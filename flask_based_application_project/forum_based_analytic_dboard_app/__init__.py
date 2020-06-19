from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import(Api, Resource, fields, marshal, reqparse)
from flask import Flask, jsonify, url_for, abort
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER_PATH = './docs/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH
db = SQLAlchemy(app)
bcrypt = Bcrypt()

migrate = Migrate(app, db)


# What is the role of LoginManager class
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from forum_based_analytic_dboard_app.view import routes
from forum_based_analytic_dboard_app.models import models