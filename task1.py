#Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

#Пример:

#               - A (3,6); B (2,1) -> 5,09
#               - A (7,-5); B (1,-1) -> 7,21

from functools import reduce
num1 = list(map(int, input('Введите две координаты первой точки: ').split()))
num2 = list(map(int, input('Введите две координаты второй точки: ').split()))
def num_range(num1, num2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda num: (num[1] - num[0])**2, zip(num1, num2))))
     return round(rng, 3)
print(num_range(num1, num2))