# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Without using minheap or maxheap
# Time complexity: O(nlogn)
# def topKFrequent(nums,k):
#     freq={}
#     for num in nums:
#         freq[num]=freq.get(num,0)+1
#     sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
#     result=[num for num,_ in sorted_freq[:k]]
#     return result
# nums=[1,1,1,2,2,3]
# k=2
# print(topKFrequent(nums,k))
# Using minheap
# Time complexity: O(nlogk)
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)  # Same as freq dictionary
    return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
# freq.items() will give us the key value pairs like (1,3),(2,2),(3,1)
# Then we will sort it based on the values and then we will return the keys
# The nlargest function will give us the k largest elements from the freq.items() list
# The key parameter is a function that takes an element from the iterable and returns a value to be used for comparison.
# It uses minheap
    