from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import(Api, Resource, fields, marshal, reqparse)
from flask import Flask, jsonify, url_for, abort
from flask_migrate import Migrate
from .views.reports import reports



from flask import Flask, session
from datetime import timedelta
app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER_PATH = './docs/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/site.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH
app.register_blueprint(reports)
db = SQLAlchemy(app)
bcrypt = Bcrypt()

migrate = Migrate(app, db)


# What is the role of LoginManager class
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.refresh_view = 'relogin'
login_manager.needs_refresh_message_category = "info"
login_manager.needs_refresh_message = (u"Session timedout, please re-login")

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

from .views import routes, reports
from .views.posts import posts
from .models import models

app.register_blueprint(posts)