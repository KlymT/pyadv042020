'''Создать список из N элементов (от 0 до n с шагом 1).
В этом списке вывести все четные значения.'''

#N = [i for i in range(0, 100) if i%2 == 0]
# print(N)
N = list (range (0, 100))
for i in N:
    if i%2 == 0:
        print(i)


