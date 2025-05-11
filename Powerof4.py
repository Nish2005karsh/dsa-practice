# Given an integer n, return true if it is a power of four. Otherwise, return false.An integer n is a power of four, if there exists an integer x such that n == 4x.
# Example 1:
# Input: n = 16
# Output: true
def isPowerofFour(n):
    if n<=0:
        return False
    while n%4==0:
        n=n//4
    return n==1
n=16
print(isPowerofFour(n))
