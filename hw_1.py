'''
Создать класс структуры данных Стек, Очередь.
Создать класс комплексного числа и реализовать для него арифметические операции
'''


class Stack:
    stack = []

    def __init__(self, name):
        self.name = name
        Stack.stack.append(self.name)
        print(f'Object {self.name} added to the stack.\nThe stack is {Stack.stack}')

    def pop(self):
        if self.name in Stack.stack:
            for i in reversed(Stack.stack):
                print(f'Object {Stack.stack.pop()} taken out from the stack.\nThe stack is {Stack.stack}')
                if i == self.name:
                    break
        else:
            print(f'Object {self.name} is out of the stack.\nThe stack is {Stack.stack}')


a = Stack('a')
b = Stack('b')
c = Stack('c')

b.pop()
c.pop()


class Line:
    line = []

    def __init__(self, name):
        self.name = name
        Line.line.append(self.name)
        print(f'Object {self.name} added to the Line.\nThe Line is {Line.line}')

    def pop(self):
        if self.name in Line.line:
            for i in Line.line:
                print(f'Object {Line.line.pop()} taken out from the Line.\nThe line is {Line.line}')
                if i == self.name:
                    break
        else:
            print(f'Object {self.name} is out of the Line.\nThe line is {Line.line}')


d = Line('a')
e = Line('b')
f = Line('c')

e.pop()
f.pop()
d.pop()


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


j = Complex(2, 1)
h = Complex(1, 2)

print(j + h)
print(j - h)
print(h / j)
print(h * j)

