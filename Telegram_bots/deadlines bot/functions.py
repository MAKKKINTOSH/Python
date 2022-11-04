import sqlite3
class DeadDb:
    """Класс для работы с базой данных бота"""

    def __init__(self, data_base):
        """подключение базы данных"""
        self.connect = sqlite3.connect('deadline_data_base.db', check_same_thread=False)
        self.cursor = self.connect.cursor()

    def make_deadline(self, object_type, deadline_type, deadline_date):
        """ввод в базу данных нового дедлайна"""
        self.cursor.execute("INSERT INTO deadline ('object_type', 'deadline_type', 'deadline_date')"
                            " VALUES (?, ?, ?)",
                            (object_type, deadline_type, deadline_date))
        return self.connect.commit()

    def show_deadline(self, object_type, deadline_type):
        """вывод в сообщении ближайшего дедлайна"""
        self.cursor.execute("SELECT deadline_date"
                            " FROM deadline "
                            "WHERE object_type = ? AND deadline_type = ?"
                            "ORDER BY deadline_date",
                            (object_type, deadline_type))
        return self.cursor.fetchone()

    def object(self, object_type):
        """вывод названия предмета"""
        self.cursor.execute("SELECT object_name"
                            " FROM object "
                            "WHERE object_type = ?",
                            (object_type,))
        return self.cursor.fetchone()

    def show_n_deadline(self, n):
        object_name = ''
        type=''
        date = ''
        self.cursor.execute("SELECT object_type FROM deadline WHERE rowid = ? ORDER BY deadline_date", (n,))
        object_name = self.cursor.fetchone()
        self.cursor.execute("SELECT object_name FROM object WHERE object_type = ?", (str(object_name)[2:-3],))
        object_name = str(self.cursor.fetchone())[2:-3]
        self.cursor.execute("SELECT deadline_type FROM deadline WHERE rowid = ? ORDER BY deadline_date", (n,))
        type = 'Д/З' if str(self.cursor.fetchone())[2:-3] == '0' else 'Л/Р'
        self.cursor.execute("SELECT deadline_date FROM deadline WHERE rowid = ? ORDER BY deadline_date", (n,))
        a = str(self.cursor.fetchone())[2:-3] #yyyy-mm-dd   ->   dd.mm.yyyy
        date = a[8]+a[9]+'.'+a[5]+a[6]+'.'+a[0]+a[1]+a[2]+a[3]
        return (f"{object_name} {type}: {date}")
    def delete_deadline(self,):
        """Удаление дедлайна"""