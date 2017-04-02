import sqlite3
from settings import *


con = sqlite3.connect(database_name)
print('%s created' % (database_name))
cur = con.cursor()
cur.executescript('''DROP TABLE IF EXISTS users;
CREATE TABLE users (id VARCHAR(20) PRIMARY KEY, date DATETIME, name VARCHAR(50), \
phone VARCHAR(10), arpu INT, soc_tariff VARCHAR (10))''')
con.commit()
print('"users" created')
con.close()
