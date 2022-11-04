import sqlite3

db = sqlite3.connect('test_data_base.db')
cursor = db.cursor()


#if(int(input())==1):
#    object_type = int(input("Введите тип предмета: "))
#    deadline_type = int(input("Введите тип: "))
#    a = str(input("Введите дату в формате dd.mm.yyyy: "))
#    deadline_date = a[6]+a[7]+a[8]+a[9]+'-'+a[3]+a[4]+'-'+a[0]+a[1]
#    cursor.execute("INSERT INTO deadline (object_id, deadline_type, deadline_date) VALUES (?, ?, ?)", (object_type, deadline_type, deadline_date))



#cursor.execute("DELETE FROM deadline WHERE deadline_date<date('now')")
object_type=str(input())
cursor.execute("SELECT rowid FROM object WHERE object_code = ?", (object_type, ))

db.commit()
print(cursor.fetchall())


#cursor.execute("""INSERT INTO object VALUES (1, 'InProf'), (2, 'Nosyreva'),
#            (3, 'English'), (4, 'Informatics'), (5, 'Math'), (6, 'BBC'),
#            (7, 'Prog'), (8, 'Physics'), (9, 'PE')""")
db.close()