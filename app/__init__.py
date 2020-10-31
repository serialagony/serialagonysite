from config import Config
from elasticsearch import Elasticsearch
from flask import Flask, request, app
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

app = Flask(__name__, template_folder=r'C:\Users\Joseph Staresinovic\website\templates')
app.config.from_object(Config)
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    if app.config['ELASTICSEARCH_URL'] else None


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = ('Please log in to access this page.')
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

from app import routes, models, errors

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Serial Agony Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # if not os.path.exists('logs'):
    #     os.mkdir('logs')
    # file_handler = RotatingFileHandler('logs/serialagony.log', maxBytes=10240,
    #                                 backupCount=10)
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # file_handler.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)

    # app.logger.setLevel(logging.INFO)
    # app.logger.info('Serial Agony startup')

    if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/serialagony.log',
                                            maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Serial Agony startup')

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'es'

from app import models




#hzwjkctywqkpdjzd

# 177bd5f38e004bb38455431bc8dec346 MS AZURE KEY 1 FOR TRANSLATOR
# fbeef34a7f7645898869027bca2539bb MS AZURE KEY 2 FOR TRANSLATOR