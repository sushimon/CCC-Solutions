l = input()
grid = [[1, 2], [3, 4]]

def h(grid):
    proxy = []
    proxy.append(grid[1])
    proxy.append(grid[0])
    return proxy

def v(grid):
    proxy = []
    proxy.append([grid[0][1], grid[0][0]])
    proxy.append([grid[1][1], grid[1][0]])
    return proxy

for i in range(len(l)):
    if l[i] == 'H':
        grid = h(grid)
    else:
        grid = v(grid)

print(str(grid[0][0]) + ' ' + str(grid[0][1]))
print(str(grid[1][0]) + ' ' + str(grid[1][1]))
