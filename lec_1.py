# Python_Lection

#советуют(visual code) установить autopep8, надо?

# print('hello world')


# value = None

# #print(type(a)) #тип переменной

# #Строки
# a = 6
# b = 123.3
# s = 'den'
# f = 'hello \nworld' # \n - вывод построчно
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s)) #Оппа
# print(f'{a} - {b} - {s}')
 
# f = True
# print(f)

# #Cписки
# list = [1,2,'3'] # у python Динамическая типизация
# col = [1,3,3,'re'] #пробел может поломать программу
# print(list)

# #Ввод и вывод данных
# #print, input

# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a,' + ',b, ' ', ' = ',a + b)

#Арифметические операции
# a = +2 #Унарный плюс
# b = -8 #Унарный минус
# c = a + b
# print(c)
# // деление в целых числах
# % остаток от деления
# ** - возведение в степень

#Также нет ограничения по хранению данных
# a = 2
# b = 800
# c = a**b
# print(c)

# a = 1.3123
# b = 3
# c = round(a*b, 5) # Функция раунд - выводит кол-в знаков
# print(c)

#Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen 

# a = 1 < 3 < 5 #тройные (и более) неравенства
# print(a)

# f = 1 > 2 or 4 < 6 #Дизъюнкия двух высказываний

# print(f) #True

# Ветвления
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input()
# if username == 'Паша':
#     print('Ура, это Паша!')
# elif username == 'Денис':
#     print('Здарова, Денис!!!')
# else:
#     print('Привет', username)

# Циклы
# #while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит ')
# print(inverted)

# #for

# list = [1,2,3,4,5,]

# for i in list:
#     print(i**2)

#Списки

# numbers = [1,2,3,4,5]
# print(type(numbers))
# print(f'{len(numbers)} len') # f' - интерполяция - для отображения текста
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors.append('gray') #добавить в конец
# colors.remove('red') #удалить

#Функции
# Это фрагмент программы используемый многократно

def f(x):  # Функция для примера
    if x ==1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))






                                                                  
