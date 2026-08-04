
#Leetcode - 1493
from typing import List
def longestSubarray(nums: List[int]) -> int:
        left = 0
        count = 0 
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1 
            while count > 1:
                if nums[left] == 0 :
                    count -= 1 
                left += 1 
            max_len = max(max_len,right-left+1)
        return max_len-1
nums = [0,1,0,1,0,1,1,1,0]
print(longestSubarray(nums))
#1004-Leetcode
from typing import List
def longestOnes(nums: List[int], k: int) -> int:
        left = 0
        count = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1 
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len
nums = [1,0,1,0,1,1,0,1,1,1,0]
k = 1
print(longestOnes(nums,k))
#930-Leetcode


