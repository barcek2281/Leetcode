class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, res = 0, 0
        d = set()

        for r in range(len(s)):
            ch = s[r]

            while ch in d:
                d.remove(s[l])
                l += 1
            
            d.add(ch)
            res = max(res, r - l + 1)
            
        return res

