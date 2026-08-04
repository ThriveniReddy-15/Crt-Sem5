#904-LeetCode
'''
from typing import List
def totalFruit(fruits: List[int]) -> int:
    freq = {}
    left = 0
    max_fruit = 0
    for right in range(len(fruits)):
        freq[fruits[right]] = freq.get(fruits[right],0)+ 1
        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]] 
            left += 1 
        max_fruit = max(max_fruit,right-left+1)
    return max_fruit 
fruits = [1,2,1]
print(totalFruit(fruits))'''
# leetcode -3
from typing import List
def lengthOfLongestSubstring(s: str) -> int:
       left ,ans = 0,0
       seen = set()
       for right in range(len(s)):
        seen.add(s[right])
        while s[right] in seen:
           left += 1
        seen.add(s[right])
        ans = max(ans,right-left+1)
       return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))