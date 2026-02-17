from typing import List, Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[List[int]], l2: Optional[List[int]]) -> List[int]:
        """
        Approach: We will use a two-pointer technique to compare elements from both lists and append the smaller one to our result list.
        
        Time Complexity: O(n + m) where n is the number of elements in l1 and m is the number of elements in l2. This is because we are doing a constant amount of work for each element in both lists.
        
        Space Complexity: O(n + m) as well, since we need to store all elements from both lists in our result list.
        """
        # Initialize an empty list to store the merged result
        result = []
        
        # Initialize two pointers, one for each list
        i, j = 0, 0
        
        # Loop until we have processed all elements in both lists
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        
        # If there are remaining elements in either list, append them to the result
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
    print(s.mergeTwoLists([], [1,2,3]))  # Expected: [1,2,3]
    print(s.mergeTwoLists([1,2,3], []))  # Expected: [1,2,3]