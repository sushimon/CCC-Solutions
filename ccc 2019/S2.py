T = int(input())
nums = [int(input()) for i in range(T)]

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False  
    return True

for i in nums:
    A = B = 0
    for Ai in range(2, i):
        sumN = i * 2
        if isPrime(Ai):
            sumN -= Ai
            A = Ai
            if isPrime(sumN):
                B = sumN
                break
    print(str(A) + " " + str(B))

# Algorithm Explanation
# Since we are solving for N = (A+B)/2, where A and B are primes, we will implement a prime number checker to check if A and B is prime.
# If N = (A+B)/2 then A+B = 2N. This means if we find a prime number for A, then B will be the difference between N and A. If the difference between N and A is a prime number, then we will have our two answers.