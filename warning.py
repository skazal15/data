import telebot
from component.contoller import bot_data
from odm.user import get_telegram
from model.user_model import User
import pywhatkit

get_telegram()

bot = telebot.TeleBot("1647991895:AAGqPjhkOSbsuSdycrLrikffs7kiR2-JTzM")
mon,per,dat,img = bot_data()

def telegram():
    for i in User.telegram:
        lines = i['telegramid']
        bot.send_message(lines, 'warning ⚠️ ,utilisasi storage sistem '+ mon +' diprediksi akan mencapai '+ per + ' pada tanggal: '+ dat)
        bot.send_message(lines, 'grafik utilisasi storage sistem '+ mon )
        bot.send_photo(lines, img)

def WA():
    for i in User.telegram:
        lines = i['waid']
        message='warning ⚠️ ,utilisasi storage sistem '+ mon +' diprediksi akan mencapai '+ per + ' pada tanggal: '+ dat
        print(message)
        pywhatkit.sendwhatmsg_instantly('+6282283027464',message,10)

telegram()
WA()



