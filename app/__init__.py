from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jqheryvv4cuxtsbd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flaskblogapp' #My SQL URI