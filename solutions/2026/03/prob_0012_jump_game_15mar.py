from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: 
            This problem can be solved by using dynamic programming. We keep track of the maximum reachable position from each position.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables to store the maximum reachable position and the current position
        max_reachable_position = 0
        current_position = 0
        
        # Initialize a variable to store the number of jumps
        num_jumps = 0
        
        # Iterate over the array
        for i in range(len(nums)):
            # If we can reach the end, break the loop
            if i > max_reachable_position:
                return -1
            
            # Update the maximum reachable position
            max_reachable_position = max(max_reachable_position, i + nums[i])
            
            # If we have reached the end of the current jump, increment the number of jumps and update the current position
            if i == current_position:
                num_jumps += 1
                current_position = max_reachable_position
        
        # Return the number of jumps
        return num_jumps