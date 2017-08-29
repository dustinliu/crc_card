from flask import Blueprint, render_template
from crc_board import app
import requests

web = Blueprint('web', __name__, url_prefix='/',
                template_folder='templates',
                static_folder='static',
                static_url_path='assets')

@web.route('boards/<id>', methods=['GET'])
def show_board(id):
    r = requests.get(app.config['BASE_URL'] + '/api/boards/' + id)
    return render_template('board.html', board=r.json())

@web.route('create_board', methods=['GET'])
def create_board():
    return render_template("create_board.html")

@web.route('/', methods=['GET'])
def index():
    r = requests.get(app.config['BASE_URL'] + '/api/boards')
    return render_template('index.html', boards=r.json())
