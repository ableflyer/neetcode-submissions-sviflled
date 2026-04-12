class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        seen = {}
        for right, c in enumerate(s):
            if seen.get(c, -1) >= left:
                left = seen[c] + 1
            res = max(res, (right-left) + 1)
            seen[c] = right
        return res