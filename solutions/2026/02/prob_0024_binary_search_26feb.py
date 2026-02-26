from typing import List, Optional

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> Optional[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.binarySearch([1, 3, 5, 7, 9], 5))  # Expected: 2
    print(s.binarySearch([1, 3, 5, 7, 9], 2))  # Expected: 1
    print(s.binarySearch([1, 3, 5, 7, 9], 10))  # Expected: -1