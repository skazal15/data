from werkzeug.utils import secure_filename
import os
from flask import Flask
Dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
root_dir = os.path.join(Dir, 'ewfs')
template_dir = os.path.join(root_dir, 'templates')
static_dir = os.path.join(root_dir,'static')
app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png','JPG','JPEG','PNG','xlsx'}
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.secret_key = 'loginner'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS