lines = int(input())
lis = []
speeds = []

for i in range(lines):
    lis.append(input().split())
    
for i in range(len(lis)):
    for x in range(len(lis[i])):
        lis[i][x] = int(lis[i][x])    
    
lis.sort()

for i in range(len(lis)-1):
    speeds.append(abs((lis[i+1][1] - lis[i][1])/(lis[i+1][0] - lis[i][0])))

print(max(speeds))