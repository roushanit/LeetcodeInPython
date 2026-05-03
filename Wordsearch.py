from collections import Counter

class Solution:
    def exist(self, board, word):
        row, col = len(board), len(board[0])

        if Counter(word) - Counter(sum(board, [])):
            return False

        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            board[r][c] = temp
            return found

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
        
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCED"

sol = Solution()
print(sol.exist(board, word))        
