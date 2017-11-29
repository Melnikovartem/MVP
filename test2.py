
import sqlite3


def AddNews(a=0, h='', t='', l=0, d=0):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("INSERT INTO NEWS (id, head,text,likes,dislikes) \
        VALUES (a, h, t, l, d) ")
    conn.commit()
    conn.close()
    return


def CreateTable():
    conn = sqlite3.connect('mydatabase.db')
    conn.execute('''CREATE TABLE NEWS
           (id             INT ,
           head           TEXT,
           text           TEXT,
           likes        INT,
           dislikes      INT);''')
    conn.commit()
    conn.close()
    return


def UpdateHead(h='', id=int):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("UPDATE NEWS set head = h where id=id")
    conn.commit()
    conn.close()
    return


def UpdateText(t='', id=int):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("UPDATE NEWS set text = t where id=id")
    conn.commit()
    conn.close()
    return


def UpdateLikes(l=0, id=int):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("UPDATE NEWS set likes = l where id=id")
    conn.commit()
    conn.close()
    return


def UpdateDislikes(d='', id=int):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("UPDATE NEWS set dislikes = d where id=id")
    conn.commit()
    conn.close()
    return


def DeleteRow(id=int):
    conn = sqlite3.connect('mydatabase.db')
    conn.execute("DELETE from NEWS where id=id;")
    conn.commit()
    conn.close()
    return


def SelectHead(id=int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("SELECT id, head, text, likes, dislikes  from NEWS")
    conn.commit()
    conn.close()
    return cursor[1]


def SelectText(id=int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("SELECT id, head, text, likes, dislikes  from NEWS")
    conn.commit()
    conn.close()
    return cursor[2]


def SelectLikes(id=int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("SELECT id, head, text, likes, dislikes  from NEWS")
    conn.commit()
    conn.close()
    return cursor[2]


def SelectDislikes(id=int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("SELECT id, head, text, likes, dislikes  from NEWS")
    conn.commit()
    conn.close()
    return cursor[3]


#следующий коментарий работает нормально, а функция addnews нет, хотя в них одно
"""
conn = sqlite3.connect('C:\Users\Lenovo\Desktop\mydatabase1.db')
conn.execute("INSERT INTO NEWS (id, head,text,likes,dislikes) \
    VALUES (3, 'jjfj', 'jfjfjf', 5, 9) ")
conn.commit()
conn.close()
"""

