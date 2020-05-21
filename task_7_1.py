'''
Написать контекстный менеджер для работы с SQLite DB.
'''

import sqlite3


class Context:

    def __init__(self, db):
        self.conn = sqlite3.connect(f'{db}')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def exe(self, sql_inq):
        res = self.cursor.execute(sql_inq)
        for date in res:
            print(date)

    def __exit__(self, *args):
        self.conn.close()


with Context('Students.db') as obj:
    obj.exe("SELECT * FROM Students left join faculty on students.student_id = faculty.student_id "
            "Left join marks on students.student_id = marks.student_id")

