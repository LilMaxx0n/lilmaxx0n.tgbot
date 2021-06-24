from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import requests
import os

BOT_TOKEN = '1782932844:AAEWIV8Bv6s6iCMju-sIcGAXLEY_aHIyRME'

updater = Updater(token=BOT_TOKEN, use_context=True)  # постоянно обновляет/бот, который ждет когда ему что-то напишут, также есть publisher

dispatcher = updater.dispatcher  # понимает, что нужно сделать на определенное действие/какую функцию вызвать на
# определенное сообщение


def start(update, context):  # update - обновляет сообщения, context - хранит бота
    reply_keyboard = ReplyKeyboardMarkup(keyboard = [['something'], ['somebody']], resize_keyboard = True, one_time_keyboard = True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я готов!", reply_markup=reply_keyboard)


start_handler = CommandHandler('start', start)  # если пользователь напишет старт, то сработает соответсвующая функция
dispatcher.add_handler(start_handler)  # ну и тут создаем само действие

updater.start_polling()
updater.idle()
