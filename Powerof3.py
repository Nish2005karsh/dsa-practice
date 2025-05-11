# Given an integer n, return true if it is a power of three. Otherwise, return false.An integer n is a power of three, if there exists an integer x such that n == 3x
# Input: n = 27
# Output: true
# Explanation: 27 = 33
def isPowerofThree(n):
    if n<=0:
        return False
    while n%3==0:
        n=n//3
    return n==1
n=27
print(isPowerofThree(n))