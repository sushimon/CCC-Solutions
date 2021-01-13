year = int(input())

while True:
    year += 1
    out = set()
    yearAsStr = str(year)
    for i in range(len(yearAsStr)):
        out.add(yearAsStr[i])
    if len(yearAsStr) == len(out):
        print(year)
        break