#!/usr/bin/env python
# coding: utf-8

# In[234]:
from route.register import register
from route.login import login
from route.home import done
from route.instanceapp import instance
from route.storage import storagelist,store,fore
from route.logout import logout
from route.edit import edit

login
register
done
edit
instance
storagelist
store
fore
logout



#@app.route('/vendor', methods=['POST','GET'])
#def vendor():
#    if not session.get('logged_in'):
#        return redirect(url_for('login')) 
#    return render_template('vendor.html', show_results="false",instances=data.instances, instancelen = len(data.instances), instance="", foldername="",measure="")
#
#@app.route('/show', methods=['POST','GET'])
#def show():
#    i = request.form['instance']
#    a = data_all[i]
#    p = period[a]
#    m = data.measure[i]
#    return render_template('vendor.html', show_results="show",instances=data.instances, instancelen = len(data.instances), instance=i, interval=p, intervallen=len(data.intervals), invervals=data.intervals, foldername=a, measure=m)
#
#
#@app.route('/add', methods=['POST','GET'])
#def add():
#    i = request.form['instance1']
#    p = request.form['interval1']
#    m = request.form['measure']
#    if 'file' not in request.files:
#        print('No file attached in request')
#        return redirect(request.url)
#    file = request.files['file']
#    if file.filename == '':
#        print('No file selected')
#        return redirect(request.url)
#    if file and allowed_file(file.filename):
#        filename = secure_filename(file.filename)
#        print(filename)
#    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#    path =(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#    print("path :",path)
#    result = path.split("/")
#    filename2 = result[-1:]
#    print("fname :" ,filename2)
#    filename1 = " ".join(filename2)
#    if i not in data.instances:
#        data.instances.append(i)
#        instances1.append(i)
#    period[filename]=p
#    data_all[i]=filename
#    data.measure[i]=m
#    print(data.instances)
#    print(instances1)
#    print(period)
#    print(data_all)
#    print(len(data.instances))
#    hit()
#    return render_template('data.html', show_results="false",instances=data.instances, instancelen = len(data.instances), instance="", foldername="",measure="")
#
#@app.route('/add1', methods=['POST','GET'])
#def add1():
#    return render_template('vendor.html', show_results="edit",instances=data.instances, instancelen = len(data.instances), instance="", intervals=data.intervals, intervallen=len(data.intervals), interval="", foldername="", measure="")
#
#@app.route('/return-files/<filename>')
#def return_files_tut(filename):
#    file_path = UPLOAD_FOLDER + '/'+filename
#    return send_file(file_path, as_attachment=True, attachment_filename='')
#
#@app.route('/logout', methods=['POST','GET'])
#def logout():
#    session['logged_in'] = False
#    return render_template('login.html')
#
#
#


