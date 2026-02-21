from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: This problem can be solved using two pointers, one at the start and one at the end of the array.
        We calculate the area of the water that can be trapped at each position and keep track of the maximum area.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers, one at the start and one at the end of the array
        left, right = 0, len(height) - 1
        # Initialize the maximum area
        max_area = 0
        # Initialize the minimum height on the left and right
        min_left, min_right = height[left], height[right]

        # Loop through the array
        while left < right:
            # If the height on the left is less than the height on the right
            if height[left] < height[right]:
                # If the height on the left is greater than the minimum height on the left
                if height[left] >= min_left:
                    # Update the minimum height on the left
                    min_left = height[left]
                else:
                    # Calculate the area of the water that can be trapped
                    max_area += min_left - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # If the height on the right is greater than the minimum height on the right
                if height[right] >= min_right:
                    # Update the minimum height on the right
                    min_right = height[right]
                else:
                    # Calculate the area of the water that can be trapped
                    max_area += min_right - height[right]
                # Move the right pointer to the left
                right -= 1

        # Return the maximum area
        return max_area