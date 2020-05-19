'''
Создать класс структуры данных Стек, Очередь.
Создать класс комплексного числа и реализовать для него арифметические операции
'''


class Stack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


print('Stack')
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.size())
print(a.pop())
print(a.size())
print('*' * 25)

class Queue:

    def __init__(self):
        self.elements = []

    def queue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


print('Queue')
b = Queue()
b.queue(1)
b.queue(2)
b.queue(3)
b.queue(4)
print(b.size())
print(b.dequeue())
print(b.size())
print('*' * 25)


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary > 0:
            return f'{self.real} + {self.imaginary}*i'
        elif self.imaginary < 0:
            return f'{self.real} - {self.imaginary*(-1)}*i'
        elif self.imaginary == 0 or self.imaginary == 0 and self.real == 0:
            return f'{self.real}'
        elif self.real == 0:
            return f'{self.imaginary}*i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )

    def __truediv__(self, other):
        return Complex(
            (self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2),
            (self.imaginary * other.real - self.real * other.imaginary)/(other.real**2 + other.imaginary**2)
        )


print('Complex')
j = Complex(2, 1)
h = Complex(1, 2)

print(j + h)
print(j - h)
print(h / j)
print(h * j)

