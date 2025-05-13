# Uncommon Words from Two Sentences
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

def uncommonWords(s1,s2):
    s1=s1.split()
    s2=s2.split()
    uncommon=[]
    s3=s1+s2
    for i in s3:
        if s3.count(i)==1:uncommon.append(i)
    return uncommon
print(uncommonWords("this apple is sweet","this apple is sour"))

