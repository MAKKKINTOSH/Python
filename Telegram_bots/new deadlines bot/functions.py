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
        return self.cursor.fetchone

    def show_n_deadlines(self, n):
        self.cursor.execute("")


    def delete_deadline(self,):
        """Удаление дедлайна"""
