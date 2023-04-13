# Найти два числа по их сумме и произведению

Sum = int(input("Enter sum "))
Mult = int(input("Enter multiplication "))
f = False
b = Sum
i = 0

for i in range (Sum):
    for i in range (Sum):
        if (i + b == Sum and i * b == Mult):
            print (f"{i} + {b} = {Sum} & {i} * {b} = {Mult}")
            f = True
            continue
    
    if (f == True):
        break

    b -= 1
    
if (f == False):
    print ("it's impossible")