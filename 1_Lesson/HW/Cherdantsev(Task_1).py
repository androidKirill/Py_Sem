# Нужно чтобы монетки лежали одной стороной, (0 - орел, 1 - решка) вывести минимальное число монет, после переворачивания которых у нас 
# все монеты лежали бы одной стороной

n = int(input("Enter count of medal "))

b = 0
c = 0

for i in range(n):
    m = int(input(f"{i + 1} medal on size - "))
    
    if (m == 0):
        b += 1
    elif (m == 1):
        c += 1

if (b - n == 0):
    print(0)
elif (c - n == 0):
    print(0)
elif (b < c):
    print(b)
elif (b > c):
    print(c)