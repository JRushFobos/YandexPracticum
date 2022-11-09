ALTER TABLE <имя таблицы> RENAME TO <новое имя таблицы>; 
ALTER TABLE <название таблицы> ADD COLUMN <имя колонки> <тип колонки>; 
ALTER TABLE <название таблицы> RENAME COLUMN <старое имя колонки> TO <новое имя колонки>;
ALTER TABLE <название таблицы> DROP COLUMN <имя колонки>; 
DROP TABLE <имя таблицы>; 

#---------------------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
ALTER TABLE ice_cream ADD COLUMN is_published INTEGER;
ALTER TABLE ice_cream ADD COLUMN is_on_main INTEGER;
''')

con.commit()
con.close()

#---------------------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
ALTER TABLE ice_cream  RENAME COLUMN  description TO specification;
''')

con.commit()
con.close()

#---------------------------------------------------------------

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
DROP TABLE ice_cream ;

''')

con.commit()
con.close()