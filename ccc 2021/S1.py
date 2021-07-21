N = int(input())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

area = 0

for i in range(len(h) - 1):
    l = h[i]
    r = h[i + 1]
    
    while l > 0 and r > 0:    
        small = min(l, r)
        area += w[i] * small
    
        l -= small
        r -= small
    
        if l > 0:
            area += (w[i] * l) / 2
        elif r > 0:
            area += (w[i] * r) / 2
        else:
            break

print(area)

# ALGORITHM 
# We can choose to calculate the area of each individual fence before moving onto the next.
# We will break up the fence into it's largest possible rectangle that can still fit within the fence.
# After calculating the area of the rectangle and adding it to the sum, we can decrement the left and right heights of the current fence being checked by the smallest of the two. The product of smallest(l, r) and the width will be the area of the largest possible rectangle that can fit within the fence. After decrementing, one of the values will be zero and the other will be non-zero. The other non-zero value will be the height of the remaining triangle. We can calculate the area of that triangle using A = (b * h) / 2, add it to the sum and finally move onto the next fence. 
# Repeat until there are no more remaining fences