class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []  # stores [start_index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = height * (i - idx)  # right boundary is i (exclusive)
                largest = max(largest, area)
                start = idx  # current bar can extend back to here

            stack.append([start, h])

        # drain
        for start, height in stack:
            area = height * (len(heights) - start)
            largest = max(largest, area)

        return largest