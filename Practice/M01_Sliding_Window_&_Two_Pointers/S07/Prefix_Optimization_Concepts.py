#Leetcode - 1480
'''
nums = [1,2,3,4]
res = [0] *len(nums)
for i in range(len(nums)):
    curr_sum = 0 
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)'''

nums = [1,2,3,4]
for i in range(len(nums)):
    nums[i] += nums[i-1]
print(nums)
#Leetcode - 1732

def largestAltitude(gain: List[int]) -> int:
    '''n = len(gain)
    alt = [0]*(n+1)
    for i in range(1,(n+1)):
        alt[i] = alt[i-1]+gain[i-1]
    return max(alt) '''
    curr_alt,max_alt = 0,0
    for ele in gain :
        curr_alt += ele
        max_alt = max(curr_alt,max_alt)
    return max_alt
gain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))
#Leetcode - 1991
def findMiddleIndex(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i in range(0,len(nums)):
        right_sum = total - nums[i] - left_sum
        if left_sum == right_sum:
            return i 
        left_sum += nums[i]
    return -1
nums = [1,-1,4]
print(findMiddleIndex(nums))
#Leetcode - 523
