from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import requests

updater = Updater(
    token='1782932844:AAEWIV8Bv6s6iCMju-sIcGAXLEY_aHIyRME',
    use_context=True
)  # постоянно обновляет/бот, который ждет когда ему что-то напишут, также есть publisher

dispatcher = updater.dispatcher  # понимает, что нужно сделать на определенное действие/какую функцию вызвать на
# определенное сообщение


def start(update, context):  # update - обновляет сообщения, context - хранит бота
    context.bot.send_message(chat_id=update.effective_chat.id, text="Для получения ссылки на создателя введите /writer")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите город для получения погоды в нем:")


def writer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://vk.com/makssk8r")


def weather(update, context):
    city = update.message.text
    w = requests.get(f'https://wttr.in/{city}?format=4')
    context.bot.send_message(chat_id=update.effective_chat.id, text=w.text)


weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
dispatcher.add_handler(weather_handler)

start_handler = CommandHandler('start', start)  # если пользователь напишет старт, то сработает соответсвующая функция
dispatcher.add_handler(start_handler)  # ну и тут создаем само действие
writer_handler = CommandHandler('writer', writer)
dispatcher.add_handler(writer_handler)

updater.start_polling()
updater.idle()
