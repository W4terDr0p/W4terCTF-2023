import sqlite3
import os

if os.path.exists('sql.db'):
    os.remove('sql.db')

conn = sqlite3.connect('sql.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE table flag(flag CHAR(255));')

cursor.execute("insert into flag(flag) VALUES ('" + os.environ.get("GZCTF_FLAG")  + "')")

conn.commit()
conn.close()
