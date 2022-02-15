from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://riham:root@127.0.0.1:3306/library'
#modify the config string with mysql connector
#testing with hardcoded sting it should be removed in other versions with env

db = SQLAlchemy(app)

from application import routes
