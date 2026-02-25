from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Recursive backtracking with bit manipulation.
        Time Complexity: O(2^n) due to the nature of the problem.
        Space Complexity: O(2^n) due to the recursive call stack.
        """
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path)
            
            # Iterate over the remaining numbers
            for i in range(start, len(nums)):
                # Add the current number to the path
                backtrack(i + 1, path + [nums[i]])
        
        # Initialize the result
        result = []
        
        # Start the backtracking process
        backtrack(0, [])
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[]]
    print(s.subsets([1]))  # Expected: [[1]]