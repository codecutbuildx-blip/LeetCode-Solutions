from typing import List, Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: We will use two pointers, one at the beginning and one at the end of the array.
        The pointer that is pointing to a higher wall will be moved towards the other pointer.
        When both pointers meet, we calculate the trapped rain water.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize two pointers, one at the beginning and one at the end of the array
        left = 0
        right = len(height) - 1

        # Initialize the maximum height on both sides
        max_left = 0
        max_right = 0

        # Initialize the total trapped rain water
        total_water = 0

        # Move the pointers towards each other
        while left < right:
            # If the left wall is shorter than the right wall, move the left pointer
            if height[left] < height[right]:
                # If the current left wall is higher than the previous maximum, update the maximum
                if height[left] > max_left:
                    max_left = height[left]
                # Otherwise, add the trapped rain water to the total
                else:
                    total_water += max_left - height[left]
                # Move the left pointer
                left += 1
            # If the right wall is shorter than or equal to the left wall, move the right pointer
            else:
                # If the current right wall is higher than the previous maximum, update the maximum
                if height[right] > max_right:
                    max_right = height[right]
                # Otherwise, add the trapped rain water to the total
                else:
                    total_water += max_right - height[right]
                # Move the right pointer
                right -= 1

        # Return the total trapped rain water
        return total_water