from typing import List, Optional

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[Optional[int]]:
        """
        Approach: This problem can be solved using a hash table or dictionary to store the indices of the elements in the list.
        Time Complexity: O(n), where n is the number of elements in the list. 
        Space Complexity: O(n), as we need to store all the elements in the hash table.

        """
        # Create an empty dictionary to store the indices of the elements
        num_dict = {}
        
        # Iterate over the list with enumerate to get both index and value
        for i, num in enumerate(numbers):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_dict:
                # If it is, return the indices of the complement and the current number
                return [num_dict[complement], i]
            
            # If not, add the current number and its index to the dictionary
            num_dict[num] = i
        
        # If no solution is found, return an empty list
        return []