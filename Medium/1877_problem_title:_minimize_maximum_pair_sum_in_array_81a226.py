# 1877. Problem Title: Minimize Maximum Pair Sum in Array
# LeetCode Link: https://leetcode.com/problems/

# Problem Title: Minimize Maximum Pair Sum in Array
# Difficulty: Medium
# Category: Array, Sorting, Two Pointers

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """
        Calculates the minimized maximum pair sum by pairing elements of the input array.

        The problem asks us to pair up elements of an array `nums` (which has an even length `n`)
        into `n/2` pairs such that the maximum sum among all these pairs is minimized.

        Approach:
        The key insight to minimize the maximum pair sum is to pair the smallest elements
        with the largest elements. Consider a sorted version of the array:
        `a_1 <= a_2 <= ... <= a_n`.

        If we pair `a_1` (smallest) with `a_n` (largest), their sum is `a_1 + a_n`.
        If we then pair `a_2` (second smallest) with `a_{n-1}` (second largest), their sum is `a_2 + a_{n-1}`.
        ... and so on, until we pair `a_{n/2}` with `a_{n/2 + 1}`.

        This greedy strategy works because:
        1. The largest element `a_n` *must* be part of some pair. To minimize the sum it contributes
           to, it should be paired with the smallest possible element available, which is `a_1`.
           Any other pairing for `a_n` (e.g., with `a_k` where `k > 1`) would result in a sum
           `a_k + a_n` which is greater than or equal to `a_1 + a_n`.
        2. Similarly, the smallest element `a_1` *must* be part of some pair. To minimize the
           sum it contributes to, it should be paired with the largest possible element available,
           which is `a_n`.

        By continuously pairing the smallest available element with the largest available element,
        we ensure that the sums created are as "balanced" as possible, thus minimizing the
        overall maximum pair sum.

        Algorithm Steps:
        1. Sort the input array `nums` in non-decreasing order. This makes the smallest
           elements accessible from the beginning and the largest elements from the end.
        2. Initialize `max_pair_sum` to 0. This variable will store the maximum sum found
           among all pairs using our strategy.
        3. Use two pointers: `left` starting at the beginning of the sorted array (index 0)
           and `right` starting at the end of the sorted array (index `n - 1`).
        4. Iterate while `left < right`:
           a. Calculate the current pair sum: `current_sum = nums[left] + nums[right]`.
           b. Update `max_pair_sum` to be the maximum of its current value and `current_sum`.
           c. Move `left` pointer one step to the right (`left += 1`).
           d. Move `right` pointer one step to the left (`right -= 1`).
           This effectively processes one pair (smallest and largest remaining) in each iteration.
        5. Once `left` is no longer less than `right` (they either cross or meet), all elements
           have been paired. Return `max_pair_sum`.
        """
        # Step 1: Sort the array to easily access smallest and largest elements.
        nums.sort()

        n = len(nums)
        max_pair_sum = 0
        
        # Step 2: Use two pointers, one starting from the beginning (smallest)
        # and one from the end (largest).
        left = 0
        right = n - 1

        # Step 3: Iterate and form pairs until the pointers cross.
        # Each iteration pairs the current smallest with the current largest.
        while left < right:
            current_sum = nums[left] + nums[right]  # Calculate current pair sum
            max_pair_sum = max(max_pair_sum, current_sum) # Update the overall maximum pair sum
            
            left += 1  # Move left pointer to the next smallest element
            right -= 1 # Move right pointer to the next largest element
            
        return max_pair_sum

# Time Complexity: O(N log N)
# The dominant operation is sorting the array, which takes O(N log N) time, where N is the number of elements in `nums`.
# The two-pointer iteration takes O(N) time as it iterates through half of the array elements.
# Therefore, the overall time complexity is O(N log N).

# Space Complexity: O(log N) or O(N)
# The space complexity depends on the sorting algorithm used. Python's `list.sort()` uses Timsort, which requires O(N)
# auxiliary space in the worst case (for certain patterns of elements) but often O(log N) in practice for arrays of
# primitive types. The two-pointer approach itself uses O(1) additional space (for `left`, `right`, `max_pair_sum`).
# Thus, the space complexity is dominated by the sorting algorithm's auxiliary space usage.

# Solved: 2026-02-15
