from flask import Blueprint, render_template

web = Blueprint('web', __name__, url_prefix='/board',
                     template_folder='templates',
                     static_folder='static')

@web.route('/<board_name>', methods=['GET'])
def show(board_name):
    return render_template('index.html')
