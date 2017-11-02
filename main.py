import os
from flask import Flask, request
import telebot
from random import randint
import requests

import syn_boobs

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

@bot.message_handler(commands=['syn'])
def synboobs(message):
	rand_val = randint(1, 12)
	boobs = syn_boobs.syn_boobs_lib[rand_val]
	bot.send_message(message.chat.id, boobs)

	
@bot.message_handler(content_types=['text'])
def srhsyn(message):
	if message.text == syn_boobs.syn_boobs_lib
	bot.send_message(message.chat.id, 'yes')
		

#ответ по слову
#@bot.message_handler(content_types=['text'])
#def answer_by_pass(message):
#	if message.text == 'сиськи' or 'Сиськи' or '1':
#		rand_val = randint(1, 76)
#		boobs_img = 'http://boobsandwinebot.freedynamicdns.net/localhost/www/boobs/' + str(rand_val) + '.jpg'
#		bot.send_photo(message.chat.id, boobs_img)


		


		

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
