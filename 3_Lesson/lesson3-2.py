"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

n = int(input())
list_1=[]
for i in range(n):
    list_1.append(int(input()))
m=int(input())
k=list_1[0]
for i in range(n):
    if abs(list_1[i]-k)<=abs(m-k):
        k=list_1[i]
            
print(k)
