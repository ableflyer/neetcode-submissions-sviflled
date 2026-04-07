class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, (r*c) - 1
        while l <= r:
            mid = (l+r)//2
            val = matrix[mid // c][mid % c]
            if val == target:
                return True
            if val > target:
                r -= 1
            else:
                l += 1
        return False