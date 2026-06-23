class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        
        # Initialize queue for BFS and count of fresh fruits
        queue = []
        fresh = 0
        
        # Step 1: Collect all rotten fruits and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Directions for 4-adjacent cells
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        
        # Step 2: BFS traversal
        while queue and fresh > 0:
            new_queue = []
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds and if fresh fruit
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rot the fruit
                        fresh -= 1
                        new_queue.append((nr, nc))
            queue = new_queue
            minutes += 1
        
        # Step 3: Return result
        return minutes if fresh == 0 else -1