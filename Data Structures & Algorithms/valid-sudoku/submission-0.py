from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)
        for r in range(0, 9):
            for c in range(0,9):
                val = board[r][c]

                if val == ".":
                    continue
                if(val in rowset[r] or val in colset[c] or val in boxset[r//3, c//3]):
                    return False
                rowset[r].add(val)
                colset[c].add(val)
                boxset[r//3, c//3].add(val)
        return True
