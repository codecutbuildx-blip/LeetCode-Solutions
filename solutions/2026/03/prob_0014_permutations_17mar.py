from typing import List, Optional
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: This problem can be solved using recursion and backtracking.
                  The idea is to generate all permutations of the input list.
        Time Complexity: O(n*n!) where n is the length of the input list.
        Space Complexity: O(n*n!) for storing the result.
        """
        # Base case: if the list has only one element, return it
        if len(nums) == 1:
            return [nums]
        
        # Initialize an empty list to store the permutations
        permutations = []
        
        # Iterate over each element in the list
        for i, num in enumerate(nums):
            # Create a new list without the current element
            remaining_nums = nums[:i] + nums[i+1:]
            
            # Generate all permutations of the remaining numbers
            for perm in self.permute(remaining_nums):
                # Add the current number to each permutation
                permutations.append([num] + perm)
        
        return permutations

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))  # Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(s.permute([0, 1]))  # Expected: [[0, 1], [1, 0]]