num1 = int(input())
num2 = int(input())

count = 2
while num1 >= num2 and num1 >= 0 and num2 >= 0:
    helper = num1 - num2
    num1 = num2
    num2 = helper
    count += 1

print(count)