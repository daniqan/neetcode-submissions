class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])

        # Initialize a simple list as queue (manual implementation)
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))  # Add all treasure chests

        # BFS directions
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        head = 0  # Manual queue pointer

        # BFS traversal
        while head < len(queue):
            r, c = queue[head]
            head += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and if cell is INF
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))