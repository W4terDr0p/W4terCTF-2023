import sqlite3
import os

if os.path.exists('sql.db'):
    os.remove('sql.db')

conn = sqlite3.connect('sql.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE flag(fl4g_1s_HeR3 CHAR(255));')

cursor.execute("insert into flag(fl4g_1s_HeR3) VALUES ('" + os.environ["GZCTF_FLAG"] + "')")

cursor.execute('''CREATE TABLE levels(
        levelname CHAR(255),
        level INT
    );
''')

cursor.execute('''insert into levels VALUES
    ('Baby',1),
    ('Trivial',2),
    ('Easy',3),
    ('Normal',4),
    ('Medium',5),
    ('Hard',6),
    ('Expert',7),
    ('Insane',8);
''')

conn.commit()
conn.close()
