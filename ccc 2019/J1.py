# scores for Apples
applesThree = int(input())
applesTwo = int(input())
applesFree = int(input())

# scores for Bananas
bananasThree = int(input())
bananasTwo = int(input())
bananasFree = int(input())

# calculate total points
applesTotal = applesThree * 3 + applesTwo * 2 + applesFree
bananasTotal = bananasThree * 3 + bananasTwo * 2 + bananasFree

# determine who won
if applesTotal > bananasTotal:
    print('A')
elif applesTotal < bananasTotal:
    print('B')
else:
    print('T')
