from flask import render_template, url_for, flash, redirect, request
from forum_based_analytic_dboard_app import app, db, bcrypt
from forum_based_analytic_dboard_app.forms import CompanyResearchForm
from forum_based_analytic_dboard_app.models.models import Company
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
# from flask_login import login_user, current_user, logout_user, login_required
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv','zip'}

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/company_research_questionaire", methods=['GET', 'POST'])
def fill_company_questionaire():

    form = CompanyResearchForm()
    
    if request.method == 'POST':

        if form.validate_on_submit():
            company = Company(name=form.company_name.data, \
                desc=form.company_desc.data, \
                
            website=form.company_website.data)
            db.session.add(company)
            db.session.commit()
            flash(f'The {form.company_name.data} \
            record has been added to the inventory', 'success')
            try:
            
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['file']
                print(file.filename.rsplit('.', 1)[1].lower())
                # if user does not select file, browser also
                # submit an empty part without filename
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)

                if file and allowed_file(file.filename):
                    # print('ho')
                    filename = secure_filename(file.filename)   
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            except IndexError:
                print("somthing went wrong")        
            
        return redirect(url_for('fill_company_questionaire'))
    return render_template('research_form.html', title='Register', form=form)


