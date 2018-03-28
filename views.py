import os

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   send_from_directory)

from config import config
from utils import dir_list

app = Flask(__name__)
app.jinja_env.variable_start_string = "{{ "
app.jinja_env.variable_end_string = " }}"
app.config.from_object(config['default'])
config['default'].init_app(app)

CURRENT_DIR = app.config.get('CURRENT_DIR')

# 跳转到/ftp
@app.route('/', methods=['GET'])
def home_of_no_variable_get():
    return render_template('app.html')
    #  return redirect('/ftp')

@app.route('/api/v3/ftp', methods=['POST'])
def info_post(path=''):
    if request.json:
        currentPath = request.json['path']
        path = os.path.join(CURRENT_DIR, currentPath)
        fileList, dirList = dir_list(path)
    return jsonify({'fileList': fileList, 'dirList': dirList})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
