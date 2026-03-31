class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                box = (i//3, j//3)
                if val in row[i] or val in col[j] or val in boxes[box]:
                    return False
                row[i].add(val)
                col[j].add(val)
                boxes[box].add(val)
        return True