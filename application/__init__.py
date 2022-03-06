from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from os import getenv


# Environmental variables need to be set at jenkins
app = Flask(__name__)
# Set login details from environment variables
user = getenv('MYSQL_USER')
password = getenv('MYSQL_PASSWORD')
mysqluri = getenv('MYSQL_URI')
x = getenv('MYSQL_DATABASE')
#secret = getenv('MYSQL_SECRETKEY')
mysql= MySQL()
# don't forget to switch
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://riham:root@127.0.0.1/library'
#app.config['SQLALCHEMY_DATABASE_URI'] = mysqluri
# Added security
app.config['SECRET_KEY'] ="aaa23782ncdjsj"

db = SQLAlchemy(app)
app.config['MYSQL_DATABASE_USER'] = getenv('MYSQL_USER')   # default user of MySQL to be replaced with appropriate username
app.config['MYSQL_DATABASE_PASSWORD'] ='root' # default passwrod of MySQL to be replaced with appropriate password
app.config['MYSQL_DATABASE_DB'] = 'library' # Database name to be replaced with appropriate database name
app.config['MYSQL_DATABASE_HOST'] =getenv('MYSQL_URL')
mysql.init_app(app)
conn = mysql.connect()

from application import routes
