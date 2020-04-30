'''Создать словарь Страна:Столица. Создать список стран. Не все
страны со списка должны сходиться с названиями стран со словаря. С
помощою оператора in проверить на вхождение элемента страны в
словарь, и если такой ключ действительно существует вывести
столицу.'''

N = dict(
    Ukraine = 'Kyiv',
    UK = 'London',
    Poland = 'Warsaw',
    CzechRepublic = 'Praha',
)


n = ['Ukraine', 'Russia', 'CzechRepublic', 'Austria', 'China']

for i in n:
    if i in N.keys():
        print(N[i])

