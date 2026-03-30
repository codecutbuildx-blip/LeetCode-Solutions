from typing import List, Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[List[int]], l2: Optional[List[int]]) -> List[int]:
        """
        Approach: We will use a two-pointer technique to compare elements from both lists and append the smaller one to our result list.
        
        Time Complexity: O(n + m), where n is the length of the first list and m is the length of the second list. This is because we are scanning through both lists once.
        
        Space Complexity: O(n + m), as in the worst case, all elements from both lists will be stored in our result list.
        """
        # Initialize an empty list to store the merged result
        merged_list = []
        
        # Initialize two pointers, one for each list
        i = j = 0
        
        # Continue the process until we have scanned through both lists
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                # If the current element in the first list is smaller, append it to our result list and move the pointer forward
                merged_list.append(l1[i])
                i += 1
            else:
                # If the current element in the second list is smaller, append it to our result list and move the pointer forward
                merged_list.append(l2[j])
                j += 1
        
        # If there are remaining elements in either list, append them to our result list
        while i < len(l1):
            merged_list.append(l1[i])
            i += 1
        while j < len(l2):
            merged_list.append(l2[j])
            j += 1
        
        # Return the merged and sorted list
        return merged_list

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1, 2, 3], [4, 5, 6]))  # Expected: [1, 2, 3, 4, 5, 6]
    print(s.mergeTwoLists([], [1, 2, 3]))  # Expected: [1, 2, 3]
    print(s.mergeTwoLists([1, 2, 3], []))  # Expected: [1, 2, 3]