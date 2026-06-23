class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        parent = [i for i in range(rows * cols + 1)]  # +1 for dummy node
        dummy = rows * cols  # index for dummy node

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union two sets
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Convert (r, c) to 1D index
        def index(r, c):
            return r * cols + c

        # Union border 'O's with dummy
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    if r in [0, rows - 1] or c in [0, cols - 1]:
                        union(index(r, c), dummy)
                    else:
                        # Union with adjacent 'O's
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                                union(index(r, c), index(nr, nc))

        # Flip enclosed 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and find(index(r, c)) != find(dummy):
                    board[r][c] = 'X'