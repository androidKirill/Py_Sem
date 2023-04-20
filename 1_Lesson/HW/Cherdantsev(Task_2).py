# Найти в строке N самое близкое (меньшее) по значению число к вводимому числу K

list_1 = [int(input(f'Enter number [{i}] ')) for i in range(0, int(input("Enter count ")))]
list_1.sort()

n = int(input("Enter number "))
if(n == 0):
    l = n + ((list_1[0] ** 2) ** 0.5)
elif(list_1[0] == 0):
    l = list_1[0] + ((n ** 2) ** 0.5)
elif ((n > 0 and list_1[0] > 0 or n < 0 and list_1[0] < 0)):
    l = (((((n ** 2) ** 0.5) - ((list_1[0] ** 2) ** 0.5)) ** 2) ** 0.5)
elif(n < 0 and list_1[0] > 0 or n > 0 and list_1[0] < 0):
    l = (((((list_1[0] ** 2) ** 0.5) + ((n ** 2) ** 0.5)) ** 2) ** 0.5)

j = list_1[0]
m = 0
for i in list_1:
    if(n == 0):
        m = n + ((i ** 2) ** 0.5)
    elif(i == 0):
        m = i + ((n ** 2) ** 0.5)
    elif(n > 0 and i > 0 or n < 0 and i < 0):
        m = (((((n ** 2) ** 0.5) - ((i ** 2) ** 0.5)) ** 2) ** 0.5)
    elif(n < 0 and i > 0 or n > 0 and i < 0):
        m = (((((i ** 2) ** 0.5) + ((n ** 2) ** 0.5)) ** 2) ** 0.5)
        
    if(m < l):
        l = m
        j = i

print(l)

print(j)