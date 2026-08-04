#Leetcode-1248
from typing import List
def numberOfSubarrays(nums: List[int], k: int) -> int:
        def sub_arr(k):
            if k < 0 :
                return 0
            left,count,odd = 0,0,0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                count += (right-left+1)
            return count
        return sub_arr(k) - sub_arr(k-1)
nums = [1,1,2,1,1]
k = 3 
print(numberOfSubarrays(nums,k))