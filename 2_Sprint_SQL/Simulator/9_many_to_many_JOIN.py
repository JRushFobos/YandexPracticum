SELECT *
-- из таблицы movies
FROM movies
-- ...но перед этим присоедини таблицу slogans так, чтобы в записях
-- совпадали значения полей movies.slogan_id и slogans.id
JOIN slogans ON movies.slogan_id = slogans.id; 

#---------------------------------------------------

SELECT movies.name,
       slogans.name
FROM movies
LEFT JOIN slogans ON movies.slogan_id = slogans.id; 

#---------------------------------------------------

SELECT movies.name,
       slogans.name
FROM movies
LEFT JOIN slogans ON movies.slogan_id = slogans.id
UNION
SELECT movies.name,
       slogans.name
FROM slogans
LEFT JOIN movies ON movies.slogan_id = slogans.id; 

#---------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name,
       wrappers.name
FROM ice_cream
JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
WHERE wrappers.name LIKE '%праздн%'
       
''')

for result in cur:
    print(result)

con.commit()
con.close()

#---------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''
SELECT  ice_cream.name,
        categories.slug,
        wrappers.name,
        MIN(ice_cream.price),
        AVG(ice_cream.price)
FROM ice_cream
JOIN categories ON ice_cream.category_id = categories.id
LEFT JOIN wrappers ON ice_cream.wrapper_id = wrappers.id
GROUP BY categories.id

''')

for result in cur:
    print(result)

con.commit()
con.close()

#---------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS toppings(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream_toppings(
id INTEGER PRIMARY KEY,
topping_id INTEGER NOT NULL,
ice_cream_id INTEGER NOT NULL,
FOREIGN KEY(topping_id) REFERENCES toppings(id),
FOREIGN KEY(ice_cream_id) REFERENCES ice_cream(id)
);
''')

con.commit()
con.close()