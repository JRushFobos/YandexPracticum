import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS types(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type_id INTEGER NOT NULL,
    FOREIGN KEY(type_id) REFERENCES types(id)
);
''')

con.commit()
con.close() 
#---------------------------------------------
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 2),
    (2, 'Весёлые мелодии', 2),
    (3, 'Кто подставил кролика Роджера', 3),
    (4, 'Хороший, плохой, злой', 3),
    (5, 'Последний киногерой', 3),
    (6, 'Она написала убийство', 4),
]
types = [
    (1, 'Мультфильм'),
    (2, 'Мультсериал'),
    (3, 'Фильм'),
    (4, 'Сериал'),
]
cur.executemany('INSERT INTO types VALUES(?, ?);', types)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close() 
#---------------------------------------------
SELECT movies.name,
       types.name
FROM movies,
     types
WHERE movies.type_id = types.id AND types.name = 'Фильм'; 

#---------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

''')

con.commit()
con.close()
#---------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       categories.slug,
       MAX(ice_cream.price)
       
FROM categories,ice_cream
WHERE ice_cream.category_id = categories.id
GROUP BY
       categories.slug
ORDER BY 
       ice_cream.price DESC;


''')

for result in cur:
    print(result)

con.commit()
con.close()