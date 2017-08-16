from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
logger = app.logger

env = getenv('CRC_CARD_ENV', 'prod')
if env == 'dev':
    app.config.from_object('config.dev')
else:
    app.config.from_object('config.prod')

db = SQLAlchemy(app)

from crc_card.web.view import web
app.register_blueprint(web)

from crc_card.api.resources import api_board

app.register_blueprint(api_board)

if env == 'dev':
    db.drop_all()
    db.create_all()