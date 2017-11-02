import os

from flask import Flask, request

import telebot
from random import randint

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']
SECRET = '/' + TOKEN


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

#приветствие, id
@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '... Твой id: ' + str(message.from_user.id))
	bot.send_message(message.chat.id, 'скоро я смогу налить тебе винца и показать пару красивых сисек!')
  

#ответ по слову
@bot.message_handler(content_types=['text'])
def answer_by_pass(message):
	if message.text == 'сиськи':
		bot.send_message(message.chat.id, "скоро тут будут сиськи")
	elif message.text == 'вино':
		bot.send_message(message.chat.id, "может быть, когда-нибудь")

		
#тестим картинку
@bot.message_handler(commands=['pic1'])
def sendPic(message):
	photo1 = open('2ch.hk/b/src/149422226/14902648817391.jpg', 'rb')
	bot.sendPhoto(message.chat.id, photo1)	
	
#тестим картинку
@bot.message_handler(commands=['pic2'])
def sendPic(message):
	photo2 = open('http://i1.perdos.me/files/video/2017/02/P7357/P7357_perdos.ru_18.jpg')
	bot.sendPhoto(message.chat.id, photo2)

#тестим картинку
@bot.message_handler(commands=['pic3'])
def sendPic(message):
	bot.sendPhoto(message.chat.id, 'https://forums.drom.ru/attachment.php?attachmentid=4955722&d=1422632931')	
	
    
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
