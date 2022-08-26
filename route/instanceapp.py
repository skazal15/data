from component.appflask import app
from flask import render_template,session,redirect,url_for
from core.analis import all_data
from odm import data
from odm.user import User
from component.contoller import dashboard

datepred,lastusage,key2,d,series1,color,predictiondat1,mse,instance,predict,d1,predictdat1,predictmax,predictmin,persen,due,predict1,mer=dashboard()
@app.route('/instance')
def instance():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    return render_template('instance.html',instancelen=len(data.instances),instances=data.instances,prediction_date=datepred,lastusage=lastusage,mer=mer,storage=User.storage )


@app.route('/process/<instancen>', methods=['POST','GET'])
def process(instancen):
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))  
    i = instancen
    mer = data.measure[i]
    for it in range(len(data.instances)):
        if i == all_data[it][7]:
            key2 = all_data[it][0]
            prediction_date = all_data[it][1]
            d = all_data[it][2]
            series1 = all_data[it][3]
            color = all_data[it][4]
            predictiondat1 = all_data[it][5]
            mse = all_data[it][6]
            instance = all_data[it][7]
            predict = round(all_data[it][8],2)
            d1 = all_data[it][9]
            predictdat1 = all_data[it][10]
    print(len(predictdat1))
    print(len(d1))
    return render_template('proses.html',key2=key2, show_results="true", instancelen = len(data.instances), instances=data.instances,
                           mse=mse,
                           predict=predict,storage=User.storage,
                           prediction_date=prediction_date, dates=d, dates2=d1, series2=predictdat1, series=series1, color=color, predictiondat=predictiondat1, instance=instance,mer=mer)
