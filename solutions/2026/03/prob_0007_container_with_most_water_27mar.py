from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int], k: int) -> int:
        """
        Approach: 
            We use a two-pointer technique to track the maximum area that can be formed between two lines.
            The left pointer starts at the beginning of the container and the right pointer starts at the end.
            We move the pointers towards each other, expanding the range of potential containers until we find the one with the most water.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize the maximum area
        max_area = 0

        # Initialize the left and right pointers
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the width of the current container
            width = right - left

            # Calculate the height of the current container (the minimum of the two lines)
            min_height = min(height[left], height[right])

            # Calculate the area of the current container
            area = min_height * width

            # Update the maximum area if necessary
            max_area = max(max_area, area)

            # Move the pointers towards each other
            if min_height == height[left]:
                left += 1
            else:
                right -= 1

        return max_area