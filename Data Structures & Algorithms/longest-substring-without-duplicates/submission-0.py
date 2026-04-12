class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        seen = {}
        for j, c in enumerate(s):
            if seen.get(c, -1) >= i:
                i = seen[c] + 1
            res = max(res, j-i+1)
            seen[c] = j
        return res