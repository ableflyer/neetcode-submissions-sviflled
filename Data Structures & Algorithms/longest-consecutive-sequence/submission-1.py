class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for i in num_set:
            if i-1 not in num_set:
                curr = 1
                while i+curr in num_set:
                    curr += 1
                if count < curr:
                    count = curr
        return count