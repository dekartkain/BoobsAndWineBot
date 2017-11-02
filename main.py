import os

from flask import Flask, request

#import dices
#import rm
import telebot
from random import randint

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']
SECRET = '/' + TOKEN


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

#приветствие, id
@bot.message_handler(commands=['start'])
def start(message):
#    bot.reply_to(message, 'Hi, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id, message.from_user.username)
  


#повторяем сообщение
@bot.message_handler(content_types=["привет"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '... Твой id: ' + str(message.from_user.id))
    bot.send_message(message.chat.id, message.text)
    
#тест
@bot.message_handler(commands=['test'])
def start(message):
#    bot.reply_to(message, 'Hi, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
    str1 = 'привет..' + message.from_user.username + ' ...123'
    bot.send_message(message.chat.id, str1)
    
#тест2
@bot.message_handler(commands=['test2'])
def start(message):
#    bot.reply_to(message, 'Hi, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + ' ...123' + str(message.from_user.id))
    bot.send_message(message.chat.id, 'привет..' + message.from_user.username + ' ...123')

#повторяем сообщение
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

    
    
    
@server.route(SECRET, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200
       
@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url=URL+SECRET)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))  
