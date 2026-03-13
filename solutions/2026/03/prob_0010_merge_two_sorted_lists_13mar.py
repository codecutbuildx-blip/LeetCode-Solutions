from typing import List, Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[List[int]], l2: Optional[List[int]]) -> List[int]:
        """
        Approach: We will use a two-pointer technique to compare elements from both lists and append the smaller one to our result list.
        
        Time Complexity: O(n + m), where n is the number of elements in l1 and m is the number of elements in l2.
        
        Space Complexity: O(n + m), as we are creating a new list with all elements from both input lists.
        """
        # Initialize an empty list to store our result
        result = []
        
        # Initialize two pointers, one for each list
        i, j = 0, 0
        
        # Continue the process until we have traversed both lists
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        
        # If there are remaining elements in either list, append them to our result
        while i < len(l1):
            result.append(l1[i])
            i += 1
        while j < len(l2):
            result.append(l2[j])
            j += 1
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1,2,3], [4,5,6]))  # Expected: [1,2,3,4,5,6]
    print(s.mergeTwoLists([], [0,1,2]))  # Expected: [0,1,2]
    print(s.mergeTwoLists([0], []))  # Expected: [0]