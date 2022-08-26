from flask import session,request,render_template,redirect,url_for
from model.user_model import User
from odm.user import Login, activity,get_rule
from component.appflask import app

@app.route('/', methods=['POST','GET'])
def login():
    session['logged_in'] = False
    username = request.form.get('username')
    password = request.form.get('password')
    if username != None and password != None:
        Login(username,password)
        if User.name == '' and User.password=='':
            return redirect(url_for('login'))
        if User.name==username and User.password==password:
            if User.catagory=='Storage maintenance':
                User.storage='yes'
            if User.catagory != 'Storage maintenance':
                User.storage='no'
            session['logged_in']=True
            get_rule(User.name)
            activity(User.name,'login')
            return redirect(url_for('done'))
    return render_template('login.html')