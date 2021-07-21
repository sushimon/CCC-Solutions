totalCap = int(input())
initial = int(input())
transmissionR = int(input())
daysPassed = 0
totalInfected = initial

while totalInfected <= totalCap:
    daysPassed +=1
    totalInfected += transmissionR ** daysPassed * initial

print(daysPassed)
