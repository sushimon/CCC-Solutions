n = int(input())
tCount = 0
sCount = 0


for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j].upper() == "S":
            sCount += 1
        elif line[j].upper() == "T":
            tCount += 1

if tCount == sCount or sCount > tCount:
    print("French")
else:
    print("English")