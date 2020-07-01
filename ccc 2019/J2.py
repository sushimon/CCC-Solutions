numLines = int(input())

lines = []
for i in range(numLines):
    lines.append(input().split())

for i in range(numLines):
    lines[i][0] = int(lines[i][0])
    print(lines[i][1] * lines[i][0])
