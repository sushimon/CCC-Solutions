n = int(input())
userResp = {}
key = {}
score = 0

for i in range(n):
    userResp[i] = input()

for i in range(n):
    key[i] = input()
    
for i in range(n):
    if userResp[i] == key[i]:
        score += 1

print(score)