#3 Лекция. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# ----Передача функции другой переменной

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))
 
# print(f(4))
# print(g(4))


# ----Функция в функции
# def calc1(x):
#     return x*2

# def calc2(x):
#     return x+10

# def math(operation,x):
#     print(operation(x))

# math(calc1,5)
# math(calc2,5)

# ---- Лямбда

# def sum(x,y):
#     return x+y

# sum = lambda x, y: x+y #смысл тот же что и у функции выше (просто короче)

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# # calc(sum, 4, 5) 
# calc(lambda x, y: x+y, 4, 5) #смысл как у выражения выше (просто избавились от описания функции)
 

# List comprehension (быстрое создание списков)

# list = []

# for i in range(1,100):
#     list.append(i)

# print(list)

# list = [i for i in range(1,101)] #Тоже самое что и выражение сверху
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21)]

# print(list)

#К чему всё это?) (Задачка)
# list1 = [1,2,3,4,5,8,12,17,21]

# def f(x):
#     return x**2

# list2 = [(i,f(i)) for i in list1 if i % 2 == 0]

# print(list2)


# # Функция map
# li = [x for x in range(1,20)] #Создаём список

# li = list(map(lambda x:x+10, li)) #К списку li применяем функцию map, а в lambda
#                                   # прописываем что будет с элементами списка

# print(li)

# #Дальше

# data = list(map(int,input().split())) 
# #Здесь функция map преобразует введеную строку(символы через пробел) в int, 
# # ну а List делает из этого список
# print(data)
# #ВАЖНО, если мы не преобразуем map в list, то эти данные
# #нигде не сохранятся, и мы их несоклько раз например не сможем вывести

# # Функция filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

# #Функция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary)) #ПОложили результат функции в data
# print(data)

#Функция enumerate

users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users)) 
print(data)







