# Given a string s consisting of words and spaces, return the length of the last word in the string.A word is a maximal substring consisting of non-space characters only.
# Ex=>Hello world Output=>5
def lengthOfLastWord(s):
    words=s.split()
    if len(words)==0:
        return 0
    return len(words[-1])
s="Hello world"
print(lengthOfLastWord(s))
