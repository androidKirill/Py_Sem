# Вывести из двух (возможно с повторениями) наборов чисел в порядке
# возрастания все те числа, которые встречаются в обоих наборах

list1 = list(set([int(input(f'Enter number [{i}] in array [1] = ')) for i in range(int(input('Enter count of array [1] - ')))]).intersection(set([int(input(f'Enter number [{i}] in array [2] = ')) for i in range(int(input('Enter count of array [2] - ')))])))

list1.sort()

for i in list1:
    print(i)