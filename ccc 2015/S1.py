# initializing what we need
lis = []

# getting input
K = int(input())

for i in range(K):
    curr = int(input())
    if curr != 0:
        lis.append(curr)
    else:
        if len(lis) > 0:
            lis.pop()

# output
print(sum(lis))