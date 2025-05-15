# Complexity is O(n^2) due to the nested loop
# def twosum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# nums=[2,7,11,15]
# target=9
# print(twosum(nums,target))
# Using hashmao
def twosum(nums,target):
    hashmap={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[num]=i
    return []
nums=[2,7,11,15]
target=9
print(twosum(nums,target))