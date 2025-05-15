from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
    
# Reverse string using Two pointer approach
# string="hello"
# def reversestring(string):
#     i=0
#     j=len(string)-1
#     while i<j:
#         string[i],string[j]=string[j],string[i]
#         i+=1
#         j-=1
#     return string
# print(reversestring(string))