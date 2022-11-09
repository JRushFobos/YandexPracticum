import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''SELECT name, text
               FROM ice_cream
               WHERE is_published= 1
               ORDER BY name DESC
               LIMIT 2 OFFSET 1
''')


for result in cur:
    print(result)


con.commit()
con.close()