from typing import List, Optional
import itertools

class Solution:
    def numDistinct(self, nums: List[int], k: int) -> int:
        """
        Approach: Use the concept of permutations and combinations to find the number of distinct permutations.
        
        Time Complexity: O(n*k), where n is the length of the input list 'nums' and k is the target length.
        
        Space Complexity: O(1), as we are not using any additional space that scales with input size.
        """
        # Initialize a variable to store the count of distinct permutations
        count = 0
        
        # Iterate over each element in the input list 'nums'
        for i in range(len(nums)):
            # Use itertools.combinations to generate all possible combinations of length k
            # and itertools.permutations to generate all possible permutations of those combinations
            for combination in itertools.combinations(nums, i):
                if len(combination) < k:
                    continue
                for permutation in itertools.permutations(combination, k):
                    # If the sorted permutation is equal to the original list, increment the count
                    if tuple(permutation) == tuple(sorted(combination)):
                        count += 1
        
        # Return the total count of distinct permutations
        return count

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct([1,2,3], 2))  # Expected: 2
    print(s.numDistinct([1,2,3], 3))  # Expected: 0
    print(s.numDistinct([1,2,3], 4))  # Expected: 0