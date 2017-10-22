# Import libraries and packages
import config, bot, main

from pyowm import *

def get_weather(text):
    obs = main.owm.weather_at_place(text)
    w = obs.get_weather()
    temp = str(round(w.get_temperature(unit='celsius').get('temp')))
    status = str(w.get_detailed_status())

    weather = "Температура: " + temp +", состояние погоды: " + status

    return (weather)
