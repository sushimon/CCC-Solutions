import sys

xCoords = []
yCoords = []
bufferNums = []
smallestX = sys.maxsize
largestX = 0
smallestY = sys.maxsize
largestY = 0

points = int(input())

for i in range (points):
    newDrop = input()
    bufferNums = newDrop.split(",")
    xCoords.append(bufferNums[0])
    yCoords.append(bufferNums[1])
    bufferNums = []

for x in xCoords:
    if int(x)>= largestX:
        largestX = int(x)
    if int(x) <= smallestX:
        smallestX = int(x)

for y in yCoords:
    if int(y)>= largestY:
        largestY = int(y)
    if int(y) <= smallestY:
        smallestY = int(y)

print(str(smallestX - 1) + "," + str(smallestY - 1))
print(str(largestX + 1) + "," + str(largestY + 1))
