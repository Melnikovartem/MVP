import config
import parser
import sqlite3

#костыль 1 conn на всегда(здесь не критично)
conn = sqlite3.connect(config.db)
c = conn.cursor()

def push():
    data = parser.get_posts()
    for post in data[::-1]:
        try:
            c.execute("INSERT INTO News ('link', 'title', 'date') VALUES ('%s', '%s', '%s')" % (post["link"], post["title"], post["date"]))
        except sqlite3.IntegrityError:
            pass
    conn.commit()
def pull():
    return c.execute("SELECT title, link FROM News WHERE pushed = 0").fetchall() 
def upd_pull(t_id, link):
    print(t_id)
    c.execute("UPDATE News SET pushed = 1, telegram_id = '%s' WHERE link = '%s'" % (t_id, link))
    conn.commit()
