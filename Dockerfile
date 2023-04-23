FROM python:3.9-alpine

COPY requirements.txt ./

RUN pip install flask && pip install -r requirements.txt && set FLASK_APP=app.py 

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]