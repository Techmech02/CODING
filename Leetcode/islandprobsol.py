class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # DFS function to explore the island
        def dfs(i, j, m, n, grid):
            # Check if the current cell is out of bounds or water (0)
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            # Mark the current cell as visited (water)
            grid[i][j] = 0
            area = 1  # Current cell counts as 1

            # Explore all four directions
            area += dfs(i - 1, j, m, n, grid)  # Up
            area += dfs(i + 1, j, m, n, grid)  # Down
            area += dfs(i, j - 1, m, n, grid)  # Left
            area += dfs(i, j + 1, m, n, grid)  # Right

            return area

        maxArea = 0
        m, n = len(grid), len(grid[0])

        # Iterate over the grid
        for i in range(m):
            for j in range(n):
                # Only start DFS when we find land (1)
                if grid[i][j] == 1:
                    currentArea = dfs(i, j, m, n, grid)
                    maxArea = max(maxArea, currentArea)

        return maxArea