from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from model.user_model import User
from odm.user import get_telegram,register_telegram

get_telegram()

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'halo, nama saya toby, saya adalah bot ewfs, saya bertugas untuk memberitahukan anda terkait forecasting instance apabila mendekati threshold')
    update.message.reply_text(f'kamu dapat bergabung dengan saya, caranya yaitu mengirimkan /join ke saya')
    
def join(update: Update, context: CallbackContext) -> None:
    user=str(update.effective_user.id)
    print(User.name)
    print(User.telegram)
    if user in User.telegram:
        update.message.reply_text(f'anda telah terdaftar')
    else:
        update.message.reply_text(f'selamat anda telah terdaftar')
        register_telegram(User.name,user)

def main() -> None:   
    updater = Updater('1647991895:AAGqPjhkOSbsuSdycrLrikffs7kiR2-JTzM')
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('join', join))
    updater.start_polling()
    updater.idle()