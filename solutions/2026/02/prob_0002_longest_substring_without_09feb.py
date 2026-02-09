from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: We will use a sliding window approach with two pointers and a set to track unique characters.
        Time Complexity: O(n)
        Space Complexity: O(min(n,m)) where n is the number of characters in the string and m is the size of the character set.
        """
        # Initialize variables
        left = 0
        max_length = 0
        char_set = set()

        # Iterate over the string
        for right, char in enumerate(s):
            # While the character is in the set, remove characters from the left
            while char in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(char)

            # Update max_length if necessary
            max_length = max(max_length, right - left + 1)

        return max_length