# numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# posSols: 1, 2, 2, 3, 3, 3, 2, 2, 1, 1

n = int(input())

if n % 5 == 2 or n % 5 == 3: print(2)
else:
    if n <= 5: 
        if n == 1: print(1)
        elif n >= 4: print(3)
    elif n > 5:
        if n % 5 == 1: print(3)
        elif n % 5 >= 4 or n % 5 == 0: print(1)