class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            n_mid = nums[mid]
            if n_mid == target:
                return mid
            
            if nums[l] <= n_mid:
                if nums[l] <= target < n_mid:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target > n_mid:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1