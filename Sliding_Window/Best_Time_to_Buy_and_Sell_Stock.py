from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = res = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] >= 0:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
        
        return res
