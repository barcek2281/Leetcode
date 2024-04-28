from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for i in cnt.values():
            if i > 1:
                return True
        return False
    
'''
217. Contains Duplicate

Given an integer array nums, return true
if any value appears at least twice in the array, 
and return false if every element is distinct.

'''