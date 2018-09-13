# Import libraries and packages
import main
import config
import crypto
import weather
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

from telegram import *
from telegram.ext import *

from geopy.geocoders import Nominatim

town = []

location_keyboard = [
    [KeyboardButton(text="Поделиться геолокацией", request_location=True)]]
location_markup = ReplyKeyboardMarkup(location_keyboard, resize_keyboard=True)
del_location_markup = ReplyKeyboardRemove()

first_keyboard = [[InlineKeyboardButton("Да", callback_data='yes')],
                  [InlineKeyboardButton("Нет", callback_data='no')]]
first_markup = InlineKeyboardMarkup(first_keyboard)

menu_keyboard = [[InlineKeyboardButton("Погода", callback_data='weather')],
                 [InlineKeyboardButton("Валюты", callback_data='stock')]]
menu_markup = InlineKeyboardMarkup(menu_keyboard)

first_stock_keyboard = [[InlineKeyboardButton("USD/RUB", callback_data='usd')],
                        [InlineKeyboardButton("EUR/USD", callback_data='eur')],
                        [InlineKeyboardButton("Crypto", callback_data='crypto')],
                        [InlineKeyboardButton("Назад", callback_data='back')]]
first_stock_markup = InlineKeyboardMarkup(first_stock_keyboard)

crypto_list = [[InlineKeyboardButton("BTC/USD", callback_data='btcusd')],
               [InlineKeyboardButton("ETH/USD", callback_data='ethusd'),
                InlineKeyboardButton("ETP/USD", callback_data='etpeth'),
                InlineKeyboardButton("XMR/USD", callback_data='xmrusd')],
               [InlineKeyboardButton("Назад", callback_data='back')]]
crypto_markup = InlineKeyboardMarkup(crypto_list)


def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.send_message(
        chat_id=chat_id,
        text="Привет. Скажи, где ты находишься?",
        reply_markup=location_markup)


def loca(bot, update):
    message = update.message
    loca = update.message.location
    chat_id = message.chat_id

    geolocator = Nominatim()
    location = geolocator.reverse(
        str(loca.latitude) + ', ' + str(loca.longitude))
    lc = location.address.split(',')[4]
    town.append(lc)
    bot.send_message(
        chat_id=chat_id,
        text=lc + '. Правильно?',
        reply_markup=first_markup)
    bot.send_message(
        chat_id=chat_id,
        text='...',
        reply_markup=del_location_markup)


def first_callback(bot, update):
    call = update.callback_query
    message = call.message
    chat_id = message.chat_id

    if call.data == 'yes':
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text='Главная страница',
            reply_markup=menu_markup)
    elif call.data == 'weather':
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text=weather.get_weather(
                town[0]),
            reply_markup=menu_markup)
    elif call.data == 'stock':
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text='Выберете нужное',
            reply_markup=first_stock_markup)
    elif call.data == 'crypto':
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text='Выберете нужное',
            reply_markup=crypto_markup)
    elif call.data == 'btcusd' or call.data == 'ethusd' or call.data == 'etpeth' or call.data == 'xmrusd':
        x = crypto.BitFinex(call.data)
        mid = x.mid()
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message.message_id,
            text='PRICE - ' + mid,
            reply_markup=crypto_markup)
