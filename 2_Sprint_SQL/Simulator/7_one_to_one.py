import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS original_names(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    original_name_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_name_id) REFERENCES original_names(id)
);
''')

con.commit()
con.close() 

#-------------------------------------------------------------
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

original_names = [
    (1, 'Last Action Hero'),
    (2, 'Murder, She Wrote'),
    (3, 'Looney Tunes'),
    (4, 'Il Buono, il brutto, il cattivo'),
    (5, 'Who Framed Roger Rabbit'),
    (6, 'Merrie Melodies')
]

movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 3),
    (2, 'Весёлые мелодии', 6),
    (3, 'Кто подставил кролика Роджера', 5),
    (4, 'Хороший, плохой, злой', 4),
    (5, 'Последний киногерой', 1),
    (6, 'Она написала убийство', 2)
]

cur.executemany('INSERT INTO original_names VALUES(?, ?);', original_names)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close() 
#-------------------------------------------------------------
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
-- Вернуть поле name из таблицы movies и поле name из original_names
SELECT movies.name,
       original_names.name
-- ...из двух таблиц
FROM movies,
     original_names
-- Выводить только те значения полей, для которых верно условие
WHERE movies.original_name_id = original_names.id
''')

con.commit()
con.close() 

#-------------------------------------------------------------
import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS wrappers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    wrapper_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(wrapper_id) REFERENCES wrappers(id)
);
    ''')
con.commit()
con.close()

#-------------------------------------------------------------
import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.execute('''
    SELECT ice_cream.name,
           wrappers.name
    FROM
        wrappers,ice_cream
    WHERE ice_cream.wrapper_id = wrappers.id
    AND wrappers.name = 'Бумажная с черепами';

''')

for result in cur:
    print(result)

con.close()