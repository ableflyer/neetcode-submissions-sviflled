class Solution:
    def canFinish(self, piles, h, k):
        total = 0
        for i in piles:
            total = total + ((i+k-1) // k)
            if total > h:
                return False
        return total <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.canFinish(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l
