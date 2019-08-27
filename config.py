import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')


    #setting up all email config variables

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'rebecca.dragon23@gmail.com'
    MAIL_PASSWORD = 'lphjftgbchgrzusj'
    ADMINS = ['rebecca.dragon23@gmail.com']
