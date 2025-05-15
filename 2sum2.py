# Program for 2sum2  using two pointers
def twosum(numbers,target):
    left=0
    right=len(numbers)-1
    while left<right:
        curr=numbers[left]+numbers[right]
        if curr==target:
            return [left+1,right+1]
        elif curr<target:
            left+=1
        else:
            right-=1
    return []
numbers=[2,7,11,15]
target=9
print(twosum(numbers,target))