class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Edge case: empty board
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        # DFS helper to mark safe 'O's connected to border
        def dfs(r, c):
            # Base case: out of bounds or not 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # Mark as temporary safe
            board[r][c] = 'T'
            # Explore neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        # Step 2: Flip surrounded 'O's and restore safe 'T's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'