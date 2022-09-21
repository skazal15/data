import pywhatkit
from component.contoller import bot_data
mon,per,dat,img = bot_data()
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
number="+6287853005400"
cap = 'grafik utilisasi storage sistem '
message='warning ⚠️ ,utilisasi storage sistem '+ mon +' diprediksi akan mencapai '+ per + ' pada tanggal: '+ dat
pywhatkit.sendwhatmsg_instantly(number,message,10,tab_close=True)
#pywhatkit.sendwhats_image(number,img,cap,10,tab_close=True)
#message = "Your message" # Type your message
#msg = MIMEMultipart()
#password = "saidf221" # Type your password 
#msg['From'] = "wilamm99@gmail.com" # Type your own gmail address 
#msg['To'] = "khan.said86@gmail.com" # Type your friend's mail address  
#msg['Subject'] = "title" # Type the subject of your message 
#msg.attach(MIMEText(message, 'plain'))
#server = smtplib.SMTP('smtp.gmail.com',587)
#server.ehlo()
#server.starttls()
#server.ehlo()
#server.login(msg['From'], password)
#server.sendmail(msg['From'], msg['To'], msg.as_string())
#server.quit()



