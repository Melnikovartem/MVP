import database as db
import bot
from time import sleep, strftime
import config
while True:
    try:
        db.push()
        for post in db.pull():
            bot.send(post)
        print("Done", strftime("%c"))
    except Exception as e:
        print("!Error", e)
    sleep(config.time_sleep)

