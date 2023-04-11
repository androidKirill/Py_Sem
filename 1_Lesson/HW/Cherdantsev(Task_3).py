'''
6-значная цифра, сумма первых трёх должна быть равна сумме последних трёх цифр
'''
print('Enter number')
a = int(input())

b = a // 1000
d1 = b // 100
e1 = b // 10 - (d1 * 10)
f1 = b - ((d1 * 100) + (e1 * 10))

sum1 = d1 + e1 + f1

c = a % 1000
d2 = c // 100
e2 = c // 10 - (d2 * 10)
f2 = c - ((d2 * 100) + (e2 * 10))

sum2 = d2 + e2 + f2

if (sum1 == sum2):
    print('Yes')
else:
    print('No')

print ()