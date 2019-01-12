import os
from flask import Flask, request
import telebot
from random import randint
import search_google.api
import requests
import giphypop

import syn_boobsandwine

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']
SECRET = '/' + TOKEN
SEACHID = os.environ['PP_BOT_SEARCH_ID']
SEARCHAPI = os.environ['PP_BOT_SEARCH_API_KEY']

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
################################################################################################################

#приветствие, id
@bot.message_handler(commands=['start', 'help'])
def start(message):
	bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '... Твой id: ' + str(message.from_user.id))
	bot.send_message(message.chat.id, 'Я бот сисек и вина!')

#выводит лист синонимов сисек
@bot.message_handler(commands=['synboobs'])
def synboobslst(message):
	for i in range(len(syn_boobsandwine.syn_boobs_lib)):
		       bot.send_message(message.chat.id, syn_boobsandwine.syn_boobs_lib[i])

#выводит лист синонимов вина
@bot.message_handler(commands=['synwine'])
def synwineslst(message):
	for i in range(len(syn_boobsandwine.syn_wine_lib)):
		       bot.send_message(message.chat.id, syn_boobsandwine.syn_wine_lib[i])

			
#парсер	сисек
#@bot.message_handler(content_types=['text'])
#def parser(message):
#	exmp = message.text
#	exmp_lower = exmp.lower() #сделать все символы строчными
##	exmp_lower_nosp = exmp_lower.replace(' ','') #удалить проблеиы (' ')
#	synboobslist = syn_boobsandwine.syn_boobs_lib #подтягиваем словарь синонимов сисек
#	synwinelist = syn_boobsandwine.syn_wine_lib #подтягиваем словарь синонимов вина
#	for i in range(len(synboobslist)):
#		if exmp_lower.find(synboobslist[i]) != -1:
#			rand_val = randint(1, 76) #кол-во фоток
#			bot.send_message(message.chat.id, str(rand_val))
#			boobs_img = 'http://boobsandwinebot.freedynamicdns.net/localhost/www/boobs/' + str(rand_val) + '.jpg'
#			bot.send_photo(message.chat.id, boobs_img)
#			break
#	for i in range(len(synwinelist)):
#		if exmp_lower.find(synwinelist[i]) != -1:
#			bot.send_message(message.chat.id, 'Я больше по сиськам..')
#			break
#GoogleImageSearch	
@bot.message_handler(commands=['img'])
def imageSearch(message):  
	msg = message.text.replace('/img','').lstrip(' ')
	if msg != " ":
		buildargs = {
			'serviceName': 'customsearch',                        
			'version': 'v1',                                 
			'developerKey': SEARCHAPI        
		}
		
		# Define cseargs for search
		cseargs = {
			'searchType': 'image',
			'q': msg,
			'cx': SEACHID
		}
		results = search_google.api.results(buildargs, cseargs)
		if len(results.links) != 0:
#			bot.send_message(message.chat.id, results.links[randint(0, len(results.links) - 1)]) 
			bot.send_photo(message.chat.id, results.links[randint(0,10])
		else:
			bot.send_message(message.chat.id, "ERROR") 
		
#	if exmp.count('сиськи') > 0
#		rand_val = randint(1, 76) #кол-во фоток
#		boobs_img = 'http://boobsandwinebot.freedynamicdns.net/localhost/www/boobs/' + str(rand_val) + '.jpg'
#		bot.send_photo(message.chat.id, boobs_img)

			 
#поиск слова в базе синонимов и вывод изображения (точное совпадение, одно слово)
#@bot.message_handler(content_types=['text'])
#def srh(message):
#	synboobslist = syn_boobs.syn_boobs_lib
#	for i in range(len(synboobslist)):
#		if message.text == synboobslist[i]:
#			rand_val = randint(1, 76) #кол-во фоток
#			boobs_img = 'http://boobsandwinebot.freedynamicdns.net/localhost/www/boobs/' + str(rand_val) + '.jpg'
#			bot.send_photo(message.chat.id, boobs_img)
		       
		

#ответ по слову из кода
#@bot.message_handler(content_types=['text'])
#def answer_by_pass(message):
#	if message.text == 'сиськи' or 'Сиськи' or '1':
#		rand_val = randint(1, 76)
#		boobs_img = 'http://boobsandwinebot.freedynamicdns.net/localhost/www/boobs/' + str(rand_val) + '.jpg'
#		bot.send_photo(message.chat.id, boobs_img)


  
	
	
	
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
