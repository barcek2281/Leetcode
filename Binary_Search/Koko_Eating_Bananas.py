from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles) + 1

        while l < r:
            m = (l + r) // 2
            t = sum(ceil(i / m) for i in piles)

            if t <= h:
                r = m
            else:
                l = m + 1
        
        return l

'''
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas 
from that pile. If the pile has less than k bananas, she eats 
all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish 
eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
