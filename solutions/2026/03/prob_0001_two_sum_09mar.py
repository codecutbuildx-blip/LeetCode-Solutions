class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement] + 1, i + 1]
            num_dict[num] = i

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [1, 2]
    print(s.twoSum([3, 2, 4], 6))  # Expected: [1, 2]