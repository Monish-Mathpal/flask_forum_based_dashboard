from flask import render_template, url_for, flash, redirect, request
from forum_based_analytic_dboard_app import app, db, bcrypt
from forum_based_analytic_dboard_app.view.forms import LoginForm, RegistrationForm
from forum_based_analytic_dboard_app.models.models import Company, User
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
import json
from flask_login import login_user, current_user, logout_user, login_required
import requests

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv','zip'}



@app.route('/', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        print("hello")
        user = User.query.filter_by(username=form.username.data).first()
        
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.username.data)
        # form.validate_username(form.username.data)
        
        user = User(username=form.username.data, email_id=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/home", methods=['GET'])
@login_required
def home():
    return render_template('home.html')


@app.route("/company_detail/<int:id>)", methods=['GET'])
@login_required
def show_report(id):
    url = f"http://127.0.0.1:8000/users/{id}"
    data = requests.get(url)   
    return render_template('company_info.html', data=data.json())


@app.route("/search", methods=['GET','POST'])
@login_required
def search():
    if request.method == 'POST':
        id = request.values['search_value']              
        return redirect(url_for('show_report', id=id))       
    return render_template('search.html')



