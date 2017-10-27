import telebot
import confog
import parser
from time import sleep
#могу запарится и сделать так, чтобы не падало каждые 3 дня (примерно), но мне лень парится с самоподписанными сертификатами
bot = telebot.TeleBot(config.token)

def post(data):
    bot.send(config.channel, "Hello")

def check():
    all_data = parser.get_posts()
    last_post_file = open("last_post", "w")
    last_post = int(last_post_file.read())
    if all_data[len(all_data) - 1]["id"] != last_post:
        last_post_file = all_data[len(all_data) - 1]["id"] 
        last_post_file.write()
        for i in list(filter(j>last_post)):
            post(i)

if __name__ == "__main__":
    if not config.single_run:
        while True:
            check()
            sleep(config.sleep_time)
    else:
        check()

