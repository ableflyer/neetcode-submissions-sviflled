class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        res = []
        n = len(nums)
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j > k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        for i in out:
            if i not in res:
                res.append(i)
        return res