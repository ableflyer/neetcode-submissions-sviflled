class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(sorted(enumerate(nums), key=lambda x: x[1]))
        i = 0
        j = len(nums) - 1
        while i < j:
            orig_i, val_i = nums[i]
            orig_j, val_j = nums[j]
            if val_i + val_j == target:
                return sorted([orig_i,orig_j])
            elif val_i + val_j < target:
                i += 1
            else:
                j -= 1
        return [0,0]
