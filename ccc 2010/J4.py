curr = [int(x) for x in input().split(" ")]

while curr[0] != 0:
    cycle = len(curr)
    posCycles = []
    lenCycles = [cycle - 2]
    change = [0] * (cycle - 2)
    
    for i in range(2, cycle):
        change[i - 2] = curr[i] - curr[i - 1]
    posCycles.append(change)
        
    for i in range(len(change)):
        for j in range(len(change) - 1, -1, -1):
            if change[i] == change[j]:
                if j - i > 0:
                    posCycles.append(change[i:j])
    
    for i in posCycles:
        check = True
        for j in range(0, len(change) - len(i), len(i)):
            if i != change[j : j + len(i)]:
                if i[:len(change) - j] != change[j: j + len(i)]:
                    check = False
                    break
        if check is True:
            lenCycles.append(len(i))
    print(min(lenCycles))
    curr = [int(x) for x in input().split(" ")]