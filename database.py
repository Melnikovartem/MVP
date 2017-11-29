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
    ans = []
    for post in c.execute("SELECT title, link FROM News WHERE pushed = 0").fetchall():
        ans.append(post)
        c.execute("UPDATE News SET pushed = 1 WHERE link = '%s'" % post[1])
    conn.commit()
    return ans
