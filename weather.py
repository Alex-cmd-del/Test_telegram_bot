import pyowm

owm = pyowm.OWM('e93121169059c904c7d14e257bd078ac', language = "ru")

place = input( 'Ваш город:')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = round(w.get_temperature('celsius')['temp'])

print("В городе " + place + " сейчас " + w.get_detailed_status())
print('Температура сейчас: ' + str(temp))

if temp < 10:
	print("На улице холодно, одевайся теплее!")

elif temp <20:
	print("На улице прохладно, одевай куртку!")

elif temp > 20:
	print("На улице жарко, шорты и футболка!")
	