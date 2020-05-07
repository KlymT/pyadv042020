'''Создать декоратор с аргументами. Который будет вызывать функцию,
определенное кол-во раз, будет выводить кол-во времени
затраченного на выполнение данной функции и её название.'''

from timeit import default_timer as timer
import math
import time

def dec(func):
    def wrap(*args, **kwargs):
        print('Начало выполнения функции, функция вычисляет Числа Фибоначи, будет выполнена 10 раз')
        start = timer()
        for i in range(1, 11):
            func(*args, **kwargs)
            print(f'функция выполнена {i}-й раз')
        end = timer()
        print(f'Функция завершена, длительность выполнения составила {end-start} секунд')
    return wrap

@dec
def fib():
    n = int(input('Начало ряда Чисел Фибоначчи - 1, 1 \nВведиде количество следующих Чисел Фибоначи, n = '))
    a = 1
    b = 1
    i = 1
    if n <= 0:
        print("Программа завершает работу")
    else:
        while i <= n:
            c = a + b
            a = b
            b = c
            print(c, end=", ")
            i += 1


fib()


