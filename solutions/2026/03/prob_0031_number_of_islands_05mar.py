from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Approach: 
        Time Complexity: O(R*C), where R is the number of rows and C is the number of columns in the grid.
        Space Complexity: O(R*C), as we need to store the visited cells in the DFS traversal.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # Expected: 1
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 3
    print(s.numIslands([["1","0","1","0","0"],["1","0","1","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))  # Expected: 2