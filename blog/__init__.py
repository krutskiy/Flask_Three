from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '50b85c0201afee753482266e5335294d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECURITY_PASSWORD_SALT = 'salt'
SECURITY_PASSWORD_HASH = 'sha512_crypt'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_messager_message_category = 'info'

from blog import routes