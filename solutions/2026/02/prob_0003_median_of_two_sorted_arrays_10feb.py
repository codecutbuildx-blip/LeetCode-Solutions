class Solution:
    def medianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Merge the two sorted arrays and find the middle element.
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # Combine the two lists into one
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        # Add any remaining elements from the lists
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        else:
            return float(merged[n // 2])

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    # Test 1
    print(s.medianSortedArrays([1,3], [2]))  # Expected: 2.0
    # Test 2
    print(s.medianSortedArrays([1,2], [3,4]))  # Expected: 2.5