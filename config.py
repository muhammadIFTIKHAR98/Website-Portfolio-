import os

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ='sqlite:///portfolio.db'   #SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    