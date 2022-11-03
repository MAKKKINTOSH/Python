import sqlite3
class dead_db:
    """Класс для работы с базой данных бота"""

    def __init__(self, data_base):
        """подключение базы данных"""
        self.connect = sqlite3.connect('deadline_data_base.db')
        self.cursor = self.connect.cursor()

    def make_deadline(self, object_type, deadline_type, deadline_date):
        """ввод в базу данных нового дедлайна"""

    def show_deadline(self, object_type, deadline_type):
        """вывод в сообщении ближайшего дедлайна"""