# prompt the user to input the number of rows and columns
numRows = int(input())
numCols = int(input())

# get the numbers within each cell
cellNums = []
currRowNums = ""
for i in range(numRows):
    cellNums.append(input().split())

# turn all the numbers into integers
for i in range(numRows):
    for y in range (numCols):
        cellNums[i][y] = int(cellNums[i][y])
        
# create a new array to keep track of possible locations to jump to
visited = []
for i in range(numRows):
    visited.append([False] * numCols)
visited[numRows-1][numCols-1] = True

# backtrack to find a path from the end
currNum = numRows * numCols
count = 0
while count < numRows:
    for x in range(numRows - 1, -1, -1):
        for y in range(numCols - 1, -1, -1):
            if cellNums[x][y] == currNum:
                visited[x][y] = True
                currNum = (x+1) * (y+1)
    count += 1

if visited[0][0] == True:
    print("yes")
else:
    print("no")
