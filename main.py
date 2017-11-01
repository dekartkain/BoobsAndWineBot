import os

from flask import Flask, request

import dices
import rm
import telebot
from random import randint

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']
SECRET = '/' + TOKEN


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Cheer, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, message.from_user.id)
    
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))  
