class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def dfs(r, c, index):
            if index == len(word):
                return True
                
            if r < 0 or c < 0 or r >= n or c >= m or board[r][c] != word[index]:
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

        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False