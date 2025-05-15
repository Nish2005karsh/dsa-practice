# # Find common chars
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# def commonChars(words):
#     common=[]
#     for i in words[0]:
#         if all(i in word for word in words):
#             common.append(i)
#             words[0]=words[0].replace(i,"",1)
# Why replace i with ""?


#     return common
# print(commonChars(["bella","label","roller"]))
# Other method
def commonChars(words):
    common=[]
    for i in words[0]:
        if all(i in word for word in words):
            common.append(i)
    return common
print(commonChars(["bella","label","roller"]))
