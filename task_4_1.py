'''
Создайте класс ПЕРСОНА с абстрактными методами, позволяющими вывести на экран информацию о персоне,
а также определить ее возраст (в текущем году).
Создайте дочерние классы:
АБИТУРИЕНТ (фамилия, дата рождения, факультет),
СТУДЕНТ (фамилия, дата рождения, факультет, курс),
ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
со своими методами вывода информации на экран и определения возраста.
Создайте список из n персон, выведите полную информацию из базы на экран, а также организуйте поиск персон,
чей возраст попадает в заданный диапазон.
'''

from datetime import date
import abc


class Person(abc.ABC):
    list = []

    @abc.abstractmethod
    def how_old(self):
        pass

    @abc.abstractmethod
    def info(self):
        pass

    @staticmethod
    def all_info(a=15, b=100):
        j = 0
        print(f'Information about all persons in the list from {a} to {b} age period:')
        for i in Person.list:
            j += 1
            if i[2] in range(a, b+1):
                if len(i) == 4:
                    print(f'{j}. Matriculant {i[0]}, wos born {i[1]}, {i[2]} years old, {i[3]} faculty')
                elif len(i) == 5:
                    print(f'{j}. Student {i[0]}, wos born {i[1]}, {i[2]} years old, {i[3]} faculty, {i[4]} course')
                elif len(i) == 6:
                    print(f'{j}. Student {i[0]}, wos born {i[1]}, {i[2]} years old, {i[3]} faculty, position is {i[4]},'
                          f' {i[5]} years experience')


class Matriculant(Person):

    def __init__(self, surname, birthday, faculty):
        self._surname = surname
        self._birthday = birthday
        self._faculty = faculty
        Person.list.append([self._surname, self._birthday, self.how_old(), self._faculty])

    def how_old(self):
        c = date.today() - self._birthday
        return c.days // 365

    def info(self):
        print(f'Information about the person:\n{self._surname}, {self._birthday}, {self.how_old()} years old, '
              f'{self._faculty} faculty')


class Student(Matriculant):

    def __init__(self, surname, birthday, faculty, course):
        Matriculant.__init__(self, surname, birthday, faculty)
        self._course = course
        Person.list[-1].append(self._course)

class Lecturer(Matriculant):

    def __init__(self, surname, birthday, faculty, position, experience):
        Matriculant.__init__(self, surname, birthday, faculty)
        self._position = position
        self._experience = experience
        Person.list[-1].extend([self._position, self._experience])


klim = Matriculant('Tribrat', date(1984, 5, 28), 'ETF')
tanya = Student('Slepko', date(1994, 9, 12), 'Economics', 22)
vova = Lecturer('Pushkin', date(1956, 7, 25), 'Math', 'Proffesor', 30)
kolya = Matriculant('Petrov', date(1980, 3, 9), 'Legal')

print(klim.how_old())
tanya.info()
print(*Person.list)
print(vova.how_old())
Person.all_info(22, 46)
Person.all_info()
