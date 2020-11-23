num = int(input())
comps = [[0] * 2 for i in range(num)]

for i in range(num):
    curr = input().split(" ")
    comps[i][0] = curr[0]
    comps[i][1] = 2 * int(curr[1]) + 3 * int(curr[2]) + int(curr[3])

if num == 0:
    pass
elif num == 1:
    print(comps[0][0])
else:
    name1 = comps[0][0]
    name2 = comps[1][0]
    score1 = comps[0][1]
    score2 = comps[1][1]
    
    for i in range(num):
        if comps[i][1] > score1 or (comps[i][1] == score1 and comps[i][0] < name1):
            name2 = name1
            score2 = score1
            name1 = comps[i][0]
            score1 = comps[i][1]
        elif comps[i][1] > score2 or (comps[i][1] == score2 and comps[i][0] < name2):
            name2 = comps[i][0]
            score2 = comps[i][1]
    
    print(name1)
    print(name2)