from datetime import datetime
from forum_based_analytic_dboard_app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forum_based_analytic_dboard_app import login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    companies = db.relationship('Company', backref='researcher', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    website = db.Column(db.String(120), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Company('{self.id}', '{self.name}', '{self.websites}','{self.desc}')"

