# Дан список чисел. Найти из них три наибольших числа

import random
list1 = []

for i in range(int(input("Enter count - "))):
    list1.append(random.randint(1,9))

print (list1)

list1.sort()

print (list1)

print(list1[-1] + list1[-2] + list1[-3])