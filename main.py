import database as db
import bot
from time import sleep, strftime
import config

def cycle():
    try:
        db.push()
        for post in db.pull():
            db.upd_pull(bot.send(post).message_id, post[1])
        print("Done", strftime("%c"))
    except Exception as e:
        print("!Error", e)

def clear_all():
    for t_id in db.tel_pub_pull():
        bot.delete(t_id)
if __name__ == "__main__":
    print("Start")
    if config.single_run:
        clear_all()
        cycle()
        print("End")
    else:
        while True:
            cycle()
            sleep(config.time_sleep)
