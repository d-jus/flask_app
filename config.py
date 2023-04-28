import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcd'
    @staticmethod
    def init_app(app):
        pass

config = {
    #'development': DevelopmentConfig,
    #'testing': TestingConfig,
    #'production': ProductionConfig,
    #'default': DevelopmentConfig,
    'test': Config
    }