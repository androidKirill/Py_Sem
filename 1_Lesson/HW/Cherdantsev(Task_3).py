# Создать калькулятор слов

symbols = list(input("Enter word "))

print(symbols)

d = {"A": 1, "a": 1, "B": 3, "b": 3, "C": 3, "c": 3, "D": 2, "d": 2, "E": 1, "e": 1,
     "F": 4, "f": 4, "G": 2, "g": 2, "H": 4, "h": 4, "I": 1, "i": 1, "J": 8, "j": 8,
     "K": 5, "k": 5, "L": 1, "l": 1, "M": 3, "m": 3, "N": 1, "n": 1, "O": 1, "o": 1,
     "P": 3, "p": 3, "Q": 10, "q": 10, "R": 1, "r": 1, "S": 1, "s": 1, "T": 1, "t": 1,
     "U": 1, "u": 1, "V": 4, "v": 4, "W": 4, "w": 4, "X": 8, "x": 8, "Y": 4, "y": 4, "Z": 10, "z": 10}

m = 0

for i in symbols:
    for key, value in d.items():
        if (i == key):
            m += int(value)

print(m)