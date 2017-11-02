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
################################################################################################################

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
@bot.message_handler(commands=['pic'])
def sendPic(message):
	img1 = bot.getuserprofilephotos(256587040)
	bot.send_message(message.chat.id, str(img1))
	#bot.sendPhoto(message.chat.id, img1)

		

#http://voshod.tk/promo/img/fin0.png
  
	
	
	
################################################################################################################	
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
