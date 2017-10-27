import telebot
import config
import parser
from time import sleep
bot = telebot.TeleBot(config.token)

def post(data):
    bot.send_message(config.channel, "Hello" + data["text"])

def check():
    all_data = parser.get_posts()
    last_post = int(open("last_post", "r").read())
    if all_data[len(all_data) - 1]["id"] != last_post:
        #f = open("last_post", "w")
        #f.write(str(all_data[len(all_data) - 1]["id"]))
        #f.close()
        for i in list(filter(lambda x: x["id"]>last_post, all_data)):
            post(i)

if __name__ == "__main__":
    if not config.single_run:
        while True:
            check()
            sleep(config.sleep_time)
    else:
        check()

