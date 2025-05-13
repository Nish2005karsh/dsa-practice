# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:

# Input: x = 123
# Output: 321
# It is basically a pallindorme questino we just need to enhance that like basically the rev should not be out of bound.so
# If reversed number < -2147483648 OR reversed number > 2147483647 → return 0
def reverse(x):
    sign=-1 if x<0 else 1
    x=abs(x)
    rev=0

    while(x!=0):
        digit=x%10
        if rev<-2147483648 or rev>2147483647:
            return 0
        rev=rev*10+digit
        x=x//10
    rev=sign*rev
    return rev
x=123
print(reverse(x))