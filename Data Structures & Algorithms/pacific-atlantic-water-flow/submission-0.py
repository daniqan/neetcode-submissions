class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case: empty grid
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])  # Grid dimensions
        pacific, atlantic = set(), set()  # Reachable cells for each ocean

        # DFS function to explore reachable cells
        def dfs(r, c, visited, prev_height):
            # Stop if out of bounds, already visited, or height < previous
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            # Explore all 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Run DFS from all Pacific border cells
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])  # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])  # Left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column

        # Intersection of reachable cells
        result = list(pacific & atlantic)
        return result