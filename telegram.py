import pyowm
import telebot

owm = pyowm.OWM('e93121169059c904c7d14e257bd078ac', language = "ru")
bot = telebot.TeleBot("924019143:AAFYqHaVYZlJROAxwRzWOltOE6rcxqMBZGA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = round(w.get_temperature('celsius')['temp'])

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status()
	answer += 'Температура сейчас: ' + str(temp) + '\n \n'

	if temp < 10:
		answer += "На улице холодно, одевайся теплее!"

	elif temp <20:
		answer += "На улице прохладно, одевай куртку!"

	else:
		answer += "На улице жарко, шорты и футболка!"
	

bot.polling( none_stop = True)
