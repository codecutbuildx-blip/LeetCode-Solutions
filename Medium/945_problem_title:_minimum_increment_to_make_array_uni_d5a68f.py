# 945. Problem Title: Minimum Increment to Make Array Unique
# LeetCode Link: https://leetcode.com/problems/

# Problem Title: Minimum Increment to Make Array Unique
# Difficulty: Medium
# Category: Array, Greedy, Sorting

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of increments required to make all elements in the array unique.

        Approach: Greedy with Sorting
        The core idea is to process the numbers in a way that minimizes increments locally,
        which leads to a global minimum due to the problem's structure.

        1. Sort the input array `nums`: This is the crucial first step. By sorting,
           we ensure that when we consider `nums[i]`, all preceding elements `nums[0]`
           through `nums[i-1]` have already been made unique and are as small as
           possible. This allows us to make greedy choices for `nums[i]`.

        2. Initialize `total_increments = 0`: This variable will accumulate the total
           number of increments performed.

        3. Initialize `expected_next_unique = 0`: This variable keeps track of the
           smallest integer value that the current number `num` (from the sorted array)
           *must* become to be unique and to accommodate the values processed so far.
           It's essentially the 'next available slot' for a unique number. We start
           at 0 because array elements are non-negative.

        4. Iterate through each `num` in the sorted array `nums`:
           a. If `num < expected_next_unique`:
              This means the current number `num` is a duplicate of a previously
              processed value, or it's too small to maintain uniqueness with the
              current sequence of numbers. To make it unique with minimum increments,
              we must increment `num` until it reaches `expected_next_unique`.
              The number of increments needed for this specific `num` is
              `expected_next_unique - num`. Add this to `total_increments`.
              After this conceptual increment, the value of this `num` is now
              `expected_next_unique`. So, the `expected_next_unique` for the
              *next* number in the array must be `expected_next_unique + 1`.
           b. If `num >= expected_next_unique`:
              This means `num` is already unique relative to all previous elements
              and is also large enough to fit into the sequence without needing
              increments. In this case, no increments are needed for `num`.
              The `expected_next_unique` for the *next* number must then be
              `num + 1` (i.e., strictly greater than the current `num`).

        This greedy strategy works because by sorting, we ensure that we address
        duplicates of smaller numbers first. For each number, we increment it
        *just enough* to make it unique and available for the next smallest slot.
        This local optimization ensures that we leave the maximum possible room
        for subsequent numbers, leading to a globally minimal number of increments.
        """
        if not nums:
            return 0

        # 1. Sort the array. This is critical for the greedy approach.
        # Processing numbers in increasing order allows us to determine the
        # minimum required value for each number based on previous elements.
        nums.sort()

        total_increments = 0
        # 2. `expected_next_unique` tracks the smallest available integer
        # that the current number `num` can take to be unique.
        # It's initialized to 0, as the smallest possible number is 0.
        expected_next_unique = 0 

        # 3. Iterate through the sorted numbers.
        for num in nums:
            if num < expected_next_unique:
                # If the current number is less than the smallest value required
                # to be unique with previous elements, we must increment it.
                # The minimum increments needed is to raise `num` to `expected_next_unique`.
                total_increments += (expected_next_unique - num)
                # After this, the slot `expected_next_unique` is now taken.
                # So, the next available unique value for subsequent numbers must be `expected_next_unique + 1`.
                expected_next_unique += 1
            else:
                # If `num` is already greater than or equal to `expected_next_unique`,
                # it means `num` is already unique and valid relative to previous elements.
                # No increments are needed for `num`.
                # The next available unique value for subsequent numbers must be strictly
                # greater than the current `num`.
                expected_next_unique = num + 1
        
        return total_increments

# Time Complexity: O(N log N)
#   The dominant factor is sorting the array, which takes O(N log N) time,
#   where N is the number of elements in `nums`.
#   The subsequent single pass iteration through the array takes O(N) time.
#   Therefore, the total time complexity is O(N log N).

# Space Complexity: O(N)
#   The space complexity primarily depends on the sorting algorithm used.
#   Python's `list.sort()` (Timsort) can use O(N) space in the worst case
#   (e.g., when merging requires temporary storage), although it's often
#   O(log N) or less in practice for nearly sorted or specific data distributions.
#   For competitive programming, it's safer to consider O(N) for list sorting.
#   The additional variables (`total_increments`, `expected_next_unique`) use O(1) space.

# Solved: 2026-02-15
