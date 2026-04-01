class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        res = []
        n = len(nums)
        for i in range(0, n-2):
            j, k = i + 1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        for i in out:
            if i not in res:
                res.append(i)
        return res