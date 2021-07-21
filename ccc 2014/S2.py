def solution():
    N = int(input())
    names1 = input().split()
    names2 = input().split()
    
    for i in range(N):
        curr = names1.index(names2[i])
        if names1[i] != names2[curr] or curr == i:
            return "bad"
    
    return "good"

print(solution())