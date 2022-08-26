from component.appflask import app
from flask import session,redirect,url_for,render_template
from component.contoller import dashboard
from odm import data
from model.user_model import User
datepred,lastusage,key2,d,series1,color,predictiondat1,mse,instance,predict,d1,predictdat1,predictmax,predictmin,persen,due,predict1,mer=dashboard()

@app.route('/done')
def done():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    username = str(session.get('user',None))
    return render_template('index2.html',show_results="false", instancelen = len(data.instances), instances=data.instances, key2="",
                    predict=predict, predictmax=predictmax,storage=User.storage,
                    prediction_date=datepred, dates=d1, color="#4747A1", predictiondat=predictdat1,max=predictmax,min=predictmin, mse=[], instance=instance,usern=User.name,due=due,lastusage=lastusage,persen=persen,mer=mer)