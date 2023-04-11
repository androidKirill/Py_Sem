# Найдите сумму трёхзначного числа

print('Enter number')
a = int(input())

b = a // 100
c = a // 10 - (b * 10)
d = a - ((b * 100) + (c * 10))

print (b + c + d)