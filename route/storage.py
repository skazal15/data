from component.appflask import app
from flask import render_template,session,url_for,redirect
from component.contoller import fore
from odm import data
mer,key2,prediction_date,d,series1,color,predictiondat1,mse,instance,predict,d1,predictdat1=fore()

@app.route('/storagelist')
def storagelist():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    return render_template('storagedash.html',storagetipelen=len(data.storagetipe),storagetipe=data.storagetipe,storage=data.storage)

@app.route('/storage')
def store():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    for i in range(0,len(data.path)):
        data.paths.append(data.path[i])
        data.sto.append(data.pasen[i])
    return render_template('prosesstorg.html',paths=data.paths,sto=data.sto,storagelen=len(data.path),storage=data.storage)


@app.route('/fore')
def forecastor():
    if not session.get('logged_in'):
        return redirect(url_for('login')) 
    if session['logged_in'] == 'false' or session['logged_in']=='':
        return redirect(url_for('login'))
    return render_template('forecasto.html',key2=key2, show_results="true", instancelen = len(data.instances), instances=data.instances,
                           mse=mse,storage=data.storage,
                           predict=predict,
                           prediction_date=prediction_date, dates=d, dates2=d1, series2=predictdat1, series=series1, color=color, predictiondat=predictiondat1, instance=instance,mer=mer)