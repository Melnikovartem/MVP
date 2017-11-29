import telebot
import config
bot = telebot.TeleBot(config.token)

def send(post):
    bot.send_message(config.channel, post[0] + "\nЧитать далее:\nhttp://lycu1580.mskobr.ru" + post[1])

