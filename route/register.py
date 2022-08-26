from component.appflask import app
from flask import render_template,request,redirect
from odm.user import Register

@app.route('/add_user',methods=['POST','GET'])
def register():
    username = request.form.get('name')
    password = request.form.get('password')
    telp = request.form.get('telp')
    email = request.form.get('email')
    gender = request.form.get('gender')
    department = request.form.get('department')
    catagory = request.form.get('role')
    group = request.form.get('group')
    Register(username,password,telp,email,gender,catagory,department,group)
    return redirect('/')

@app.route('/register',methods=['POST','GET'])
def page_register():
    return render_template('register.html')
