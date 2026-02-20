from typing import List, Optional

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # Sort the candidates array
        candidates.sort()
        
        # Initialize the result list
        result = []
        
        # Define a helper function for backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
        
        # Start the backtracking process
        backtrack(target, [], 0)
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))  # Expected: [[2,2,3],[7]]
    print(s.combinationSum([2,3,5], 8))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]
    print(s.combinationSum([2], 1))  # Expected: []