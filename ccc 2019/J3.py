numLines = int(input())

lines = []
for i in range(numLines):
    y = input()
    lines.append(y)
    
for i in range(numLines):
    curr = lines[i]
    text = ''
    counter = 0
    for x in range(len(curr)):
        if x != len(curr) - 1 and curr[x] == curr[x+1]:
            counter += 1
        else:
            text += str(counter + 1) + ' ' + curr[x] + ' '
            counter = 0
    print(text[:len(text) - 1])
