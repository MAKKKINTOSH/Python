import sqlite3

db = sqlite3.connect('test_data_base.db')
cursor = db.cursor()

cursor.execute("SELECT * FROM object WHERE object_code = 'Math' OR object_code = 'English'")
a = cursor.fetchall()[1]
print(a[0],a[1],a[2], type(a[0]))
