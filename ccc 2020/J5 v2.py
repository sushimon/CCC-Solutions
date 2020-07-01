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

# create a new array to keep track of cells that have already been visited
visited = []
for i in range(numRows):
    visited.append([False] * numCols)
visited[numRows-1][numCols-1] = True

valuesThatExit = [numRows * numCols] # any value in this list will lead to the exit
while True:
    newEntriesAdded = 0
    for x in range(numRows):
        for y in range(numCols):
            if not visited[x][y] and cellNums[x][y] in valuesThatExit:
                visited[x][y] = True
                valuesThatExit.append((x+1) * (y+1))
                newEntriesAdded += 1

    # exit if no new numbers are added
    if newEntriesAdded == 0:
        break

if visited[0][0]:
    print("yes")
else:
    print("no")
