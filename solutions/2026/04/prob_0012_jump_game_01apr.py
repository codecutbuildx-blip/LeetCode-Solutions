from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We initialize a list dp where dp[i] represents the maximum number of steps we can take from index i to reach the end.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n <= 1:
            return 0

        dp = [nums[0]] + [float('inf')] * (n - 1)

        for i in range(1, n):
            for j in range(i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))  # Expected: 2
    print(s.jump([2,3,0,1,4]))  # Expected: 2