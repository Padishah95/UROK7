#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
#day = int(input('Введите день недели: '))
#if day > 7 or day < 1:
 #   print('Введите правильность дня недели,от 1 до 7')
#elif day == 6 or day == 7:
 #   print("Ура, это выходной!")
#else:
 #   print("Нет,это не выходной=((( !")

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#x = int(input('Введите число x '))
#y = int(input('Введите число y '))
#z = int(input('Введите число z '))

#a = x * y * z
#b = x + y + z

#if a > 0:
     #a = 0
#elif a < 1:
     #a = 1
#if b > 0:
     #b = 1
#elif b < 1:
 #    b = 1

#if a == b:
 #   print('Утверждение истинно')
#elif a != b:
 #   print('Утверждение ложно')

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# x = int(input('input x: '))
# y = int(input('input y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')

#  Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('input quarter number: '))
# if n < 1 or n > 4:
#     print('Please, repeat the input')
# elif n == 1:
#     print('x > 0 and y > 0')
# elif n == 2:
#     print('x < 0 and y > 0')
# elif n == 3:
#     print('x < 0 and y < 0')
# elif n == 4:
#     print('x > 0 and y < 0')

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.


#def input_numbers(x): 
    #xy = ["X", "Y"]
   #for i in range(x):
       # reality = False
        #while not reality:
            #try:
                #number = int(input(f"Введите координату {xy[i]}: "))
                #a.append(number)
               # reality = True
           # except ValueError:
               # print("Не та цифра, что после запятой идет. Цифра та, что без запятых")
    #return a


#def Length(a, b):  
   # lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
   # return lengthSegment


#print("Введите координаты точки А")
#pointA = input_numbers(2)
#print("Введите координаты точки В")
#pointB = input_numbers(2)

#print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")