from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: 
            We use a greedy algorithm to solve this problem. The idea is to always choose the next position that will allow us to reach the farthest point.
            If there are multiple options, we choose the one with the maximum reachable value.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables
        n = len(nums)
        if n <= 1:
            return 0

        max_reach = nums[0]
        step = nums[0]
        res = nums[0]

        for i in range(1, n):
            if i == n - 1:
                return res + 1
            # If we can reach the current index from previous steps, update max_reach and step
            if i <= max_reach:
                max_reach = max(max_reach, i + nums[i])
                step -= 1
            # If we cannot reach the current index from previous steps, try to find a new path
            else:
                res += 1
                if step == 0:
                    return -1

        return res