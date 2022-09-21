from component.appflask import app
from flask import render_template,session,redirect,url_for
from core.analis import all_data,doc
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
    if data.tipe[i] == 'real':
        for it in range(len(data.instances)-1):
            if i == all_data[it][7]:
                key2 = all_data[it][0]
                prediction_date = all_data[it][1]
                dates = all_data[it][2]
                series1 = all_data[it][3]
                series1 = series1[0]
                color = all_data[it][4]
                predictiondat1 = all_data[it][5]
                predictiondat1 = predictiondat1[0]
                mse = all_data[it][6]
                instance = all_data[it][7]
                predict = round(all_data[it][8],2)
                dates2 = all_data[it][9]
                predictdat1 = all_data[it][10]
                high = max(predictdat1)
                low = 0
                if high < 100:
                    stepsize = 10
                    high = high + 10
                if high < 1000:
                    stepsize = 100
                    high = high + 100
                else:
                    stepsize = 1000
                    high = high + 2000
    else:
        color = '#FFA646'
        mse = 0
        high = 1500
        low = 0
        stepsize = 100
        key2,instance,prediction_date,predict,dates,series1,predictiondat1,predictdat1,dates2,predictmax=doc(i)
    print(len(predictdat1))
    print(len(d1))
    return render_template('proses.html',key2=key2, show_results="true", instancelen = len(data.instances), instances=data.instances,
                           mse=mse,high=high,low=low,stepsize=stepsize,
                           predict=predict,storage=User.storage,
                           prediction_date=prediction_date, dates=dates, dates2=dates2, series2=predictdat1, series=series1, color=color, predictiondat=predictiondat1, instance=instance,mer=mer)
