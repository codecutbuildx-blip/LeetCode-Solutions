class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming. The idea is to create a 2D array where each cell represents the number of unique paths to reach that cell. The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left.

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Create a 2D array to store the number of unique paths to reach each cell
        dp = [[0]*n for _ in range(m)]

        # Initialize the first row and column of the array
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the rest of the array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The number of unique paths to reach the bottom-right cell is the answer
        return dp[m-1][n-1]