'''
Задача на журавликов: сделано n-ое количество журавликов, 
3 человека - 2 сделали одинаковое количество, 
3-ий сделал в два раза больше чем предыдущие в сумме
'''
i = False

while (i == False):
    print ("Enter number of birds")
    n = int(input())
    if (n % 6 == 0):
        i = True
    else:
        print('Solution is impossible.')

a = (n // 6)
b = (a * 2) * 2

print(f'Serega and Petya made {a} (both {a + a}), Katya made {b}')