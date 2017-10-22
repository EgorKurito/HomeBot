# Import libraries and packages
import main, config, crypto

from telegram import *
from telegram.ext import *

from geopy.geocoders import Nominatim

location_keyboard = KeyboardButton(text="send_location", request_location=True)
custom_keyboard = [[location_keyboard]]
reply_markup = ReplyKeyboardMarkup(custom_keyboard)

def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.send_message(chat_id = chat_id, text = "Hello", reply_markup=reply_markup)


def loca(bot, update):
    message = update.message
    loca = update.message.location
    chat_id = message.chat_id

    geolocator = Nominatim()
    location = geolocator.reverse(str(loca.latitude) + ', ' + str(loca.longitude))
    testlocation = geolocator.reverse("52.509669, 13.376294")
    bot.send_message(chat_id = chat_id, text = location.address)

    lc = location.address.split(',')
    lc1 = testlocation.address.split(',')
    print(lc[4])
    print(lc1[4])
