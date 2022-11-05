import sqlite3

db = sqlite3.connect('test_data_base.db')
cursor = db.cursor()

cursor.execute("SELECT * FROM object")
a = "(0, '2022-11-15')"
print(a.replace('0', 'Д/З'))
