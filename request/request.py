from telegram import update
from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler

with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def startcmd(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WOW")

start_handler = CommandHandler('start', startcmd)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()