class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows, cols = len(grid), len(grid[0])
        total_islands = 0

        def dfs(row, col):
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == '0' or
                (row, col) in visited
            ):
                return

            visited.add((row, col))
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    total_islands += 1
                    dfs(row, col)

        return total_islands