from flask import Blueprint, render_template

web = Blueprint('web', __name__, url_prefix='/',
                     template_folder='templates',
                     static_folder='static',
                    static_url_path='assets')

@web.route('/board/<board_name>', methods=['GET'])
def show(board_name):
    return render_template('index.html')

@web.route('/', methods=['GET'])
def index():
    return render_template('index.html')
