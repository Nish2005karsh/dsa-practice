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
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
def kthSmallest(matrix,k):
    n=len(matrix)
    left=matrix[0][0]
    right=matrix[n-1][n-1]
    while left<right:
        mid=(left+right)//2
        count=0
        j=n-1
        for i in range(n):
            while j>=0 and matrix[i][j]>mid:
                j-=1
            count+=j+1
        if count<k:
            left=mid+1
        else:
            right=mid
    return left
matrix=[[1,5,9],[10,11,13],[12,13,15]]
k=8
print(kthSmallest(matrix,k))