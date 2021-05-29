class Solution(object):

        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        
        def dfs(grid, visited, i ,j):
            visited[i][j] = 1
            if i > 0 and grid[i-1][j] == "1" and visited[i-1][j] == 0:
                dfs(grid, visited, i-1 ,j)
            if i < len(grid)-1 and grid[i+1][j] == "1" and visited[i+1][j] == 0:
                dfs(grid, visited, i+1 ,j)
            if j > 0 and grid[i][j-1] == "1" and visited[i][j-1]  == 0:
                dfs(grid, visited, i ,j-1)
            if j < len(grid[0])-1 and grid[i][j+1] == "1" and visited[i][j+1] == 0:
                dfs(grid, visited, i ,j+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    visited[i][j] = 1
                elif grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    dfs(grid, visited, i, j)
                        
        return count