''' Создать класс автомобиля. Описать общие аттрибуты. Создать классы легкового автомобиля и грузового. Описать в основном классе базовые аттрибуты для автомобилей. Будет плюсом если в классах наследниках переопределите методы базового класса.'''


class Autos:
	description = 'The is the class for autos'
	
	def __init__(self, model, vin):
		self.model = model
		self.vin = vin
	
	def auto(self):
		print(f'{Autos.description}, model = {self.model}, vin = {self.vin}')
		
car1 = Autos('mazda', '120984')

car1.auto()


class Truck(Autos):
	description = 'The is the subclass for cargo autos'
	
	def auto(self):
		print(f'{Truck.description}, model = {self.model}, vin = {self.vin}')
		
car2 = Truck('volvo', '25789')

car2.auto()


class Car(Autos):
	description = 'The is the subclass for passengers autos'
	
	def auto(self):
		print(f'{Car.description}, model = {self.model}, vin = {self.vin}')
		
car3 = Car('lexus', '267800')

car3.auto()


