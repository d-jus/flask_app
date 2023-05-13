from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_required, LoginManager, login_user, logout_user
from neural_network.display import display_error, check_crfp, check_crfm
from neural_network import compute

import os, sys
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#config block  or app.config['SECRET_KEY'] = 'abcd'
from config import config
app.config.from_object(config['test'])

#bootstrap
bootstrap = Bootstrap(app)

#bazadanych
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#logowanie
login_manager = LoginManager()
login_manager.login_view = 'formula_logo'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Prediction(db.Model):
    __tablename__ = 'prognoza'
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(64), unique=True)
    CRFp = db.Column(db.String(64), unique=False)
    CRFm = db.Column(db.String(64), unique=False)
    
    def __repr__(self):
        return f'<Prediction - place: {self.place},CRFm {self.CRFm}, CRFp {self.CRFp}>'

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Prediction=Prediction)

class NameForm(FlaskForm):
    name = StringField('Podaj wartości wskaźników?', validators=[DataRequired()])
    submit = SubmitField('Oblicz wartość wskaźników')
class WForm(FlaskForm): 
    massage = "Wymagane dane do obliczenia CRFp"
    input_1 = FloatField('Wskaźnik nr 1', validators =[DataRequired(message=massage)])
    input_2 = FloatField('Wskaźnik nr 2', validators =[DataRequired(message=massage)])
    input_3 = FloatField('Wskaźnik nr 3', validators =[DataRequired(message=massage)])
    input_4 = FloatField('Wskaźnik nr 4', validators =[DataRequired(message=massage)])
    input_5 = FloatField('Wskaźnik nr 5', validators =[DataRequired(message=massage)])
    input_6 = FloatField('Wskaźnik nr 6', validators =[DataRequired(message=massage)])
    input_7 = FloatField('Wskaźnik nr 7', validators =[DataRequired(message=massage)])
    input_8 = FloatField('Wskaźnik nr 8', validators =[DataRequired(message=massage)])
    input_9 = FloatField('Wskaźnik nr 9', validators =[DataRequired(message=massage)])
    input_10 = FloatField('Wskaźnik nr 10', validators =[DataRequired(message=massage)])
    input_11 = FloatField('Wskaźnik nr 11')
    input_12 = FloatField('Wskaźnik nr 12')
    input_13 = FloatField('Wskaźnik nr 13')
    input_14 = FloatField('Wskaźnik nr 14')
    input_15 = FloatField('Wskaźnik nr 15', validators =[DataRequired(message=massage)])
    input_16 = FloatField('Wskaźnik nr 16', validators =[DataRequired(message=massage)])
    submit = SubmitField('COMPUTE')

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('Nie można odczytać atrybutu password.')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username} oraz hasło {self.password_hash}>'

@app.route('/')
def index():
    return redirect(url_for('formula_logo'))

@app.route('/form_ex', methods=['GET', 'POST'])
def form_ex_():
    form_ex = WForm()
    if form_ex.validate_on_submit():
        in_keys = form_ex.data.keys()
        input_list = list(form_ex.data.values())[:-2]
        print("TU patrz", form_ex.data.keys())
        print("TU patrz 1a", list(form_ex.data.values())[:-2])
        try:
            if check_crfm(in_keys,input_list):
                CRFm = compute.compute_m(form_ex)
            else: CRFm = None
            if check_crfp(in_keys,input_list):
                CRFp = compute.compute_p(form_ex)
            else: raise Exception('nie obliczono')
            print('działa - zapisano do bazy')
            db.session.add(
                Prediction(
                place = f'test {datetime.now().strftime("%H:%M:%S")}',
                CRFp = CRFp, # from neural network - temp
                CRFm = CRFm # from neural network - temp
                )
            )
            db.session.commit()
            flash(f"{list(form_ex.data.values())[:-2]}, wskaźniki: {CRFp}, {CRFm}",  'alert alert-warning')
            flash(list(form_ex.data.values())[:-2], 'alert alert-success')
            flash(list(form_ex.data.values())[:-2], 'alert alert-danger')
            flash(display_error(list(form_ex.data.values())[:-2]), 'alert alert-danger') # dodałęm
        except:
            print('nie działa')
            flash(sys.exc_info()[1],'alert alert-danger')
            
    return render_template('form_ex.html', form = form_ex)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/formularz', methods=['GET', 'POST'])
def formula():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        if session.get('name') == 'Mandalorian':
           flash('CRFp - 0.56 CRFm - 0.6')
        return redirect(url_for('formula'))
    return render_template('form.html', form=form, name=session.get('name'))

@app.route('/formularz2', methods=['GET', 'POST'])
def formula2():
    form = NameForm()
    if form.validate_on_submit():
        input = Prediction.query.filter_by(place=form.name.data).first() # .CRFp
        flash(str(input))
        return redirect(url_for('formula2'))
    return render_template('form.html', form=form, name=session.get('name'))


@app.route('/database')
@login_required
def database_read():
    marks=Prediction.query.all()
    return render_template('database_table.html', marks= marks)

@app.route('/secret')
@login_required
def secret():
    return 'Dostęp tylko dla zalogowanych użytkowników!'

from auth import forms
@app.route('/logo', methods=['GET', 'POST'])
def formula_logo():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            print(request.args.get('next'))
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        flash('Nieprawidłowe dane logowania')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Zostałeś wylogowany.') # nie działa jak ma
    return redirect(url_for('formula_logo'))


"""Mando = User(username = "Mando")
Mando.password = "hello"
k1 = Prediction(place = "K1", CRFp = "3", CRFm = "6")
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(Mando)
    db.session.add(k1)
    db.session.commit()
    print("TU patrz", Prediction.query.all())"""