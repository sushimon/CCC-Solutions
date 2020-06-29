small = int(input())
med = int(input())
large = int(input())

happiness = small + 2 * med + 3 * large
if happiness >= 10:
    print("happy")
else:
    print("sad")
