from typing import List, Optional

class Solution:
    def medianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Binary Search
        Time Complexity: O(log(min(n, m)))
        Space Complexity: O(1)
        """
        # merge and sort the two arrays
        merged = sorted(nums1 + nums2)
        
        # find the length of the merged array
        n = len(merged)
        
        # if the length is odd, return the middle value
        if n % 2 == 1:
            return float(merged[n // 2])
        
        # if the length is even, return the average of the two middle values
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.medianSortedArrays([1, 3], [2]))  # Expected: 2.0
    print(s.medianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5
    print(s.medianSortedArrays([1, 2, 3, 4], [5, 6]))  # Expected: 2.5