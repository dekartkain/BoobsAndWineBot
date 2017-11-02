import os

from flask import Flask, request

#import dices
#import rm
import telebot
import pywapi
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
  


@bot.message_handler(content_types=['text'])
def handle_text(message):
	city = pywapi.get_location_ids(message.text)
	for i in city:
		cityCode = i
		weather_com_result = pywapi.get_weather_from_weather_com(cityCode)
		weatherReport = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + message.text + "." + "\n" + "Feels like " + weather_com_result['current_conditions']['feels_like'] + "°C. \n" + "Last update - " + weather_com_result['current_conditions']['last_updated']
		bot.send_message(message.chat.id, weatherReport)


#ответ по слову
#@bot.message_handler(content_types=['123', 'привет', 'hi'])
#def answer_by_pass(message):
#	bot.reply_to(message, "good")
    

#повторяем сообщение
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)

    
    
    
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
