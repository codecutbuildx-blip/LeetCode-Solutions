from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two pointers technique with two lines of code optimization.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(height) - 1
        
        # Initialize maximum area
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the width and height of the current container
            width = right - left
            h = min(height[left], height[right])
            
            # Update the maximum area if necessary
            max_area = max(max_area, width * h)
            
            # Move the pointer with the smaller height towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(s.maxArea([1,1]))  # Expected: 1
    print(s.maxArea([4,3,2,1,4]))  # Expected: 16