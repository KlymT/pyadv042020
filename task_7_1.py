'''
Написать контекстный менеджер для работы с SQLite DB.
'''

import sqlite3


class StudentsContext:

    def __init__(self):
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def exe(self, sql_inq):
        res = self.cursor.execute(sql_inq)
        for date in res:
            print(date)

    def __exit__(self, *args):
        self.conn.close()


with StudentsContext() as obj:
    obj.exe("SELECT * FROM Students left join faculty on students.student_id = faculty.student_id "
            "Left join marks on students.student_id = marks.student_id")

