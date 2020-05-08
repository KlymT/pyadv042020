'''Создать класс точки, реализовать конструктор который инициализирует 3 координаты (x, y, z). Реалзиовать методы для получения и изменения каждой из координат. Перегрузить для этого класса методы сложения, вычитания, деления, умножения. Перегрузить один любой унарный метод.
Ожидаемый результат: умножаю точку с координатами 1,2,3 на другую точку с такими же координатами, получаю результат 1, 4, 9.'''
 
 
class Point:

	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	def __str__(self):
		return (f'({self.x}, {self.y}, {self.z})')

		
	def get_x(self):
		return self.x
		
	def set_x(self, value):
		self.x = value
		
	def get_y(self):
		return self.y
		
	def set_y(self, value):
		self.y = value
		
	def get_z(self):
		return self.z
		
	def set_z(self, value):
		self.z = value
		
	def __add__(self, other):
		return Point(
			self.x + other.x,
			self.y + other.y,
			self.z + other.z
			)
			
	def __sub__(self, other):
		return Point(
			self.x - other.x,
			self.y - other.y,
			self.z - other.z
			)
			
	def __truediv__(self, other):
		return Point(
			self.x / other.x,
			self.y / other.y,
			self.z / other.z
			)
			
	def __mul__(self, other):
		return Point(
			self.x * other.x,
			self.y * other.y,
			self.z * other.z
			)
			
	def un(self):
		return Point(
			- self.x,
			- self.y,
			- self.z
			)


a = Point(4, 5, 6)
b = Point(1, 2, 3)

print(f'a  = {a.x, a.y, a.z}')
print(f'b  = {b.x, b.y, b.z}')

print(f'a + b = {a+b}')
print(f'a - b = {a-b}')
print(f'a / b = {a/b}')
print(f'a * b = {a*b}')

print(f'- a = {a.un()}')
print(f'- b = {b.un()}')

