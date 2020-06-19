from datetime import datetime
# from forum_based_analytic_dboard_app import db
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=True)
    email_id = Column(String, unique=True, index=True)
    password_hash = Column(String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)






# class Company(Base):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True, nullable=False)
#     website = db.Column(db.String(120), unique=True, nullable=False)
#     desc = db.Column(db.String(120), unique=True, nullable=False)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return f"Company('{self.id}', '{self.name}', '{self.websites}','{self.desc}')"

