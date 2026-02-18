class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        This algorithm works by scanning through the array and at each step finding the maximum sum of subarray ending at that point.
        It keeps track of the current sum and the maximum sum seen so far, updating them as it scans through the array.
        """
        # Initialize variables to keep track of the current sum and the maximum sum
        curr_sum = max_sum = nums[0]
        
        # Iterate over the array starting from the second element
        for num in nums[1:]:
            # Update the current sum by adding the current number
            # If the current sum becomes negative, reset it to the current number
            curr_sum = max(num, curr_sum + num)
            
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, curr_sum)
        
        # Return the maximum sum found
        return max_sum

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([2, -3, 4, -1]))  # Expected: 6
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6