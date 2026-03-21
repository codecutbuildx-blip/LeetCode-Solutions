from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: This problem is a classic example of dynamic programming and backtracking.
        We will use a recursive approach to generate all possible combinations and then filter out the ones that sum up to the target.

        Time Complexity: O(n*m*target), where n is the number of candidates, m is the maximum value in candidates, and target is the target sum.
        Space Complexity: O(target), as we need to store the result for each sub-problem.
        """
        # Sort the candidates array
        candidates.sort()
        
        # Initialize an empty list to store the result
        result = []
        
        # Define a helper function to perform the recursive backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remaining sum is zero, it means we have found a valid combination
                result.append(list(comb))
                return
            elif remain < 0:
                # If the remaining sum is negative, it means the current combination exceeds the target
                return
            for i in range(start, len(candidates)):
                # Add the current candidate to the current combination
                comb.append(candidates[i])
                
                # Recursively call the backtrack function with the updated remaining sum and the new start index
                backtrack(remain - candidates[i], comb, i)
                
                # Remove the last added candidate from the current combination (backtracking)
                comb.pop()
        
        # Call the backtrack function with the initial values
        backtrack(target, [], 0)
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,5], 8))  # Expected: [[2,2,2,2],[3,5]]
    print(s.combinationSum([2,3,6,7], 7))  # Expected: [[2,2,3],[7]]