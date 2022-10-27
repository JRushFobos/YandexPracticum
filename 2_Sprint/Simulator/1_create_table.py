import sqlite3
con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    bithday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

con.commit()
con.close() 