# Import libraries and packages
import config, bot, weather
import logging

from telegram import *
from telegram.ext import *
from pyowm import *

# Main variable
updater = Updater(token=config.BOT_TOKEN)

owm = OWM(config.WEATHER_TOKEN, language='ru')

# Bot authentication
root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', bot.start))
    dp.add_handler(MessageHandler(Filters.location, bot.loca))
    dp.add_handler(CallbackQueryHandler(callback=bot.first_callback))
    # dp.add_handler(MessageHandler(Filters.text, bot.loca))
    # dp.add_handler(CallbackQueryHandler(bot.callback))

    updater.start_polling()


if __name__ == '__main__':
    main()
