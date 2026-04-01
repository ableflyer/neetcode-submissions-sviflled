class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            min_height = min(heights[l], heights[r])
            area = min_height * (r-l)
            print(area, l, r)
            maxA = max(maxA, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxA