from flask import session,render_template
from component.appflask import app
from odm import data
@app.route('/logout', methods=['POST','GET'])
def logout():
    session['logged_in'] = False
    data.storage = "no"
    return render_template('login.html')