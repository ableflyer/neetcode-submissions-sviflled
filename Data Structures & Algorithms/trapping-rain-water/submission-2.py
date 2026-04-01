class Solution:
    def trap(self, height: List[int]) -> int:
        nh = len(height)
        rain_water = 0
        for i in range(1, nh):
            max_right = 0
            max_left = 0
            for j in range(i+1, nh):
                if height[j] > max_right:
                    max_right = height[j]
            for j in range(0, i):
                if height[j] > max_left:
                    max_left = height[j]
            rain_water += max(0, min(max_right, max_left)-height[i])
        return rain_water