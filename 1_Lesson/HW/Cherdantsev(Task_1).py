# Найти, сколько раз в строке N длиной F встречается число A

list_1 = [int(input(f'Enter number [{i}] ')) for i in range(int(input('Enter count ')))]

n = int(input('Enter number to find '))

list_2 = [n == list_1[i] for i in range(0, len(list_1))]

print(sum(list_2))