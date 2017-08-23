from flask import Blueprint, render_template, request
from crc_board import app
import requests

web = Blueprint('web', __name__, url_prefix='/',
                     template_folder='templates',
                     static_folder='static',
                    static_url_path='assets')

@web.route('boards/<id_or_name>', methods=['GET'])
def show_board(id_or_name):
    return render_template('index.html')

@web.route('create_board', methods=['GET'])
def create_board():
    return render_template("create_board.html")

@web.route('/', methods=['GET'])
def index():
    r = requests.get(app.config['BASE_URL'] + '/api/boards')
    return render_template('index.html', boards=r.json())
