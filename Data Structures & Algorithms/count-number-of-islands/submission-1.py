class Solution:

    def expand(self, grid,i,j):
        m,n = len(grid),len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.expand(grid,i+1,j)
        self.expand(grid,i-1,j)
        self.expand(grid,i,j+1)
        self.expand(grid,i,j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):    
                if grid[i][j] == '0':
                    continue
                
                count += 1
                self.expand(grid,i,j)
        return count