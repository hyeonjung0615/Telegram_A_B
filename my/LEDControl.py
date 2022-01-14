from typing import _get_type_hints_obj_allowed_types
from telegram.ext import Updater
from telegram.ext import CommandHandler
import RPi.GPIO as GPIO
import time


pins = (16, 15, 13) # R.G.B

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

pins = (16, 15, 13) # R.G.B


updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def startcmd(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="LED MODE")
    

def RED_ON(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="RED ON")
    GPIO.output(pins[0], GPIO.HIGH)

def RED_OFF(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="RED OFF")
    GPIO.output(pins[0], GPIO.LOW)

def GREEN_ON(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="GREEN ON")
    GPIO.output(pins[1], GPIO.HIGH)

def GREEN_OFF(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="GREEN OFF")
    GPIO.output(pins[1], GPIO.LOW)

def BULE_ON(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BULE ON")
    GPIO.output(pins[2], GPIO.HIGH)

def BULE_OFF(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BULE OFF")
    GPIO.output(pins[2], GPIO.LOW)

start_handler = CommandHandler('start', startcmd)
REDon_handler = CommandHandler('REDon', RED_ON)
REDoff_handler = CommandHandler('REDoff', RED_OFF)
GREENon_handler = CommandHandler('GREEon', GREEN_ON)
GREENoff_handler = CommandHandler('GREEoff', GREEN_OFF)
BULEon_handler = CommandHandler('BULEon', BULE_ON)
BULEoff_handler = CommandHandler('BULEoff', BULE_OFF)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(REDon_handler)
dispatcher.add_handler(REDoff_handler)
dispatcher.add_handler(GREENon_handler)
dispatcher.add_handler(GREENoff_handler)
dispatcher.add_handler(BULEon_handler)
dispatcher.add_handler(BULEoff_handler)


updater.start_polling()
updater.idle()