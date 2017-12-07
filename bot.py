import telebot
import config
from urllib import request
import json 
bot = telebot.TeleBot(config.token)

def send(post):
    return bot.send_message(config.channel, post[0] + "\nЧитать далее:\nhttp://lycu1580.mskobr.ru", reply_markup = message_markup(post[1]))

def delete(t_id):
    bot.delete_message(config.channel, t_id)
def message_markup(url_ending):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text = "Подробнее", url = googl_short("http://lycu1580.mskobr.ru" + url_ending))
    markup.add(button)
    return markup

def googl_short(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=%s' % config.google_api_key
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = request.Request(
        post_url,
        json.dumps(postdata).encode("ascii"),
        headers
    )
    ret = request.urlopen(req).read()
    return json.loads(ret)['id']
