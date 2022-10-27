import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''SELECT category, AVG(price)
               FROM ice_cream
               GROUP BY category
               HAVING category = 'Обычное');
               ''')


for result in cur:
    print(result)


con.commit()
con.close()