year = int(input())

while True:
    year += 1
    yearAsStr = str(year)
    out = set(yearAsStr)
    if len(yearAsStr) == len(out):
        print(year)
        break
