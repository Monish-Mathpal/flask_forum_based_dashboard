
from flask_restful import(Api, Resource, fields, marshal, reqparse)
from flask import Flask, jsonify, url_for, abort
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # new
from flask_marshmallow import Marshmallow
# from forum_based_analytic_dboard_app.models.models import Company 
import os

PATH = '../../'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(PATH, 'site.db') # new
db = SQLAlchemy(app) # new
ma = Marshmallow(app)
api = Api(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    website = db.Column(db.String(120), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)
#     # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     # password = db.Column(db.String(60), nullable=False)
#     # posts = db.relationship('Post', backref='author', lazy=True)

#     # def __repr__(self):
#     #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class CompanySchema(ma.Schema):
    class Meta:
        fields = ("name", "website")

company_schema = CompanySchema()
company_schema = CompanySchema(many=True)

class CompnyListResource(Resource):
    def get(self):
        companies = Company.query.all()
        return company_schema.dump(companies)


api.add_resource(CompnyListResource, '/api/v1.0/companies')


if __name__ == '__main__':
    app.run(debug=True, port=8000)