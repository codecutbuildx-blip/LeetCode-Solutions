from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two pointers technique with a two-pointer approach to track the maximum area.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers at both ends of the array
        left = 0
        right = len(height) - 1
        
        max_area = 0
        
        while left < right:
            # Calculate the width and height of the current area
            width = right - left
            water_height = min(height[left], height[right])
            
            # Update the maximum area if necessary
            max_area = max(max_area, width * water_height)
            
            # Move the pointer with the smaller height towards the other end
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(s.maxArea([1,1]))  # Expected: 1