# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.
def isugly(n):
    if n<=0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n=n//i
    return n==1
n=6
print(isugly(n))
