# Вывести все степени двойки, не превосходящие ввёденое число

n = int(input('Enter number '))

m = 1
fm = False

while(n > m):
    if (m == 1 and fm == False):
        fm = True
    else:
        m *= 2    
        
    if (m < n):
        print (m)