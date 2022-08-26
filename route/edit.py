from component.appflask import app
from flask import render_template,session,redirect,url_for
from odm.user import User

@app.route('/edit')
def edit():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    return render_template('data.html',storage=User.storage)