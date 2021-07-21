M = int(input())
N = int(input())
K = int(input())

grid = {}

# True - Gold
# False - Black
# changing the colours
for i in range(M):
    for j in range(N):
        grid[(i,j)] = False

for i in range(K):
    command = input().split()
    loc, idx = command[0], int(command[1]) - 1
    
    if loc == "R":
        for j in range(N):
            curr = grid[(idx,j)]
            grid[(idx,j)] = not(grid[(idx,j)])
    
    elif loc == "C":
        for i in range(M):
            curr = grid[(i,idx)]
            grid[(i,idx)] = not(grid[(i,idx)])

# count the number of GOLD (True)
count = 0

for i in range(M):
    for j in range(N):
        if grid[(i,j)]:
            count += 1

print(count)