'''Создать класс магазина. Конструктор должен инициализировать значения: «Название магазина» и «Количество проданных товаров». Реализовать методы объекта, которые будут увеличивать кол-во проданных товаров, и реализовать вывод значения переменной класса, которая будет хранить общее количество товаров проданных всеми магазинами.'''


class Shop:
	sumsales = 0
	
	def __init__(self, name, sales):
		self.name = name
		self.sales = sales
	
	def getsales(self):
		Shop.sumsales += self.sales
		return Shop.sumsales
		
				
atb = Shop('ATB', 25)

megm = Shop('Megamatket', 11)

megm.getsales()
atb.getsales()

print(Shop.sumsales)
