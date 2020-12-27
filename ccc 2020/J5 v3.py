rows = int(input())
cols = int(input())

grid = [list(map(int, input().split())) for i in range(rows)]

visited = {}
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        visited[(r,c)] = False

def dfs():
    q = [(1, 1)]
    while q:
        r, c = q.pop()
        visited[(r, c)] = True
        currVal = grid[r - 1][c - 1]
        if currVal == rows * cols:
            return 'yes'
        else:
            for x in range(1, rows + 1):
                if currVal % x == 0:
                    for y in range(1, cols + 1):
                        if (currVal // x) < y:
                            break
                        if x * y == currVal:
                            if visited[(x,y)] == False:
                                q.append((x,y))
    return 'no'

print(dfs())

# EXPLANATION
# Algorithm
# We're not finding the shortest path to escape but rather whether or not it is possible to escape so it'd make more intuitive sense to fully traverse one path of the grid before backtracking and checking another possible path. Using DFS (Depth-First Search) allows us to explore all possible paths of the grid to determine whether or not there is a solution. 
# After implementing a stack, we check if the value of the current cell matches the exit condition. If not we will find any possible neighbours of the current cell (cells whose product of its coordinates equals the value in the current cell), and add them to the stack if they have not been visited already.

# Optimization
# Some optimization was done during the nested for loop. We only iterated through the outer for loop if the value of the current cell was divisible by x. If it's not divisible then no values of x would satisfy x * y = currVal so there's no need to check them.
# Similar logic was used for the inner for loop. We only iterated through values of y that were less than or equal to the quotient of currVal / x. If the y value is greater than the quotient then no values of y would satisfy x * y = currVal so there's no need to check them.
# As for checking whether a cell was visited or not, we used a dictionary due to its pretty fast lookup times - average time complexity of O(1)