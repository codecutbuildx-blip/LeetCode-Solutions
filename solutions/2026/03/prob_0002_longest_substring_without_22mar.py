from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: This problem can be solved using a sliding window approach with the help of two pointers.
        We maintain a set to store unique characters in the current substring. When we encounter a repeating character,
        we move the left pointer of the window to the right until the repeating character is out of the window.

        Time Complexity: O(n)
        Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.
        """
        # Initialize variables
        max_length = 0
        char_set = set()
        left = 0

        # Iterate over the string
        for right in range(len(s)):
            # While the current character is in the set, move the left pointer to the right
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length