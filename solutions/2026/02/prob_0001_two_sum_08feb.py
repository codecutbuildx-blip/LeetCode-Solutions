from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[Optional[int]]:
        """
        Approach: Create a dictionary to store the numbers we have seen so far and their indices.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    # Test 1
    print(s.twoSum([2,7,11,15], 9))  # Expected: [0,1]
    # Test 2
    print(s.twoSum([3,2,4], 6))  # Expected: [1,2]