class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        islands = 0  # Counter for number of islands
        
        # DFS helper to mark connected land
        def dfs(r, c):
            # Base case: stop if out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # Mark current cell as visited
            grid[r][c] = "0"
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                # Found an unvisited land cell
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands