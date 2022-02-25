from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv
# Environmental variables need to be set at jenkins
app = Flask(__name__)
# Set login details from environment variables
#user = getenv('MYSQL_USER')
#password = getenv('MYSQL_PASSWORD')
#url = getenv('MYSQL_URL')
#db = getenv('MYSQL_DATABASE')
#secret = getenv('MYSQL_SECRETKEY')

# don't forget to switch
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://riham:root@127.0.0.1/library'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + user + ':' + password + '@' + url + '/' + db
# Added security
app.config['SECRET_KEY'] ="aaa23782ncdjsj"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'

from application import routes
