# get the num of rows and cols
rows = int(input())
cols = int(input())

# create the grid 
grid = [list(map(int, input().split())) for i in range(rows)]

# create a dict to later check if a cell was visited
visited = {}
for r in range(rows):
    for c in range(cols):
        visited[(r,c)] = False

# find if there's a solution using dfs
def dfs():
    q = [(rows-1, cols-1)]
    while q:
        r, c = q.pop()
        visited[(r, c)] = True
        if r == 0 and c == 0:
            return 'yes'
        else:
            neighbours = [(x, y) for x in range(rows) for y in range(cols) if grid[x][y] == (r+1)*(c+1)]
            for neighbour in neighbours:
                if visited[neighbour] == False:
                    q.append(neighbour)
    return 'no'

print(dfs())