my_dict = {'Ivan': 1982, 'Alex': 1993, 'Egor': 2004}    #создание переменной и присвоение ей словаря
print('Dict:', my_dict)                                 #вывод на экран словаря
print('Existing value:', my_dict['Ivan'])               #вывод на экран значения по существующему ключу
my_dict_1 = my_dict.get('Anna')
print('Not existing value:', my_dict_1)                 #вывод на экран значения по отсутствующему ключу
my_dict.update({'Mari': 1990, 'Lida': 1999})            #добавление в элементов в словарь
my_dict_ = my_dict.pop('Egor')                          #удаление пары в словаре по существующему ключу
print('Deleted value:', my_dict_)                       #вывод значения удаленной пары
print('Modified dictionary:', my_dict)                  #вывод на экран словаря

my_set = {1, 8.3, 4, 3, 4, 1, 'adcd', False}            #создание переменной и присвоение ей множества
print('Set:', my_set)                                   #вывод на экран множества
my_set.add('apple')                                     #добавление элемента в множество
my_set.add(True)                                        #добавление элемента в множество
my_set.remove('adcd')                                   #удаление элемента из множества
print('Modified:', my_set)                              #вывод на экран измененного множества

