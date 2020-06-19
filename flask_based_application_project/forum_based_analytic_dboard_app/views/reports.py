from flask import (Blueprint, render_template, request, redirect, \
    url_for)

import requests
from flask_login import login_required
reports = Blueprint('reports', __name__)



@reports.route("/company_detail/<int:id>)", methods=['GET'])
@login_required
def show_report(id):
    url = f"http://127.0.0.1:8000/users/{id}"
    data = requests.get(url)
    print(id)   
    return render_template('company_info.html', data=data.json())


@reports.route("/search", methods=['GET','POST'])
@login_required
def search():
    if request.method == 'POST':
        id = request.values['search_value']              
        return redirect(url_for('reports.show_report', id=id))
    return render_template('search.html')
