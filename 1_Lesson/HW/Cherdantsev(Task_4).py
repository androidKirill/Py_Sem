# Шоколадка размером m x n долек, можно разделить её один раз между дольками (на 2 прямоугольника). Сколько долек можно отколоть таким образом?

print('Enter width')
m = int(input())

print('Enter height')
n = int(input())

print('How many slices do you want to get?')
k = int(input())

if (k % m == 0 or k % n == 0 ):
    print('It\'s possible')
else:
    print('It\'s impossible')