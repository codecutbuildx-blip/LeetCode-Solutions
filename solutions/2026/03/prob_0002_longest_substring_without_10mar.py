from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: We use a sliding window approach with a set to keep track of unique characters.
        Time Complexity: O(n)
        Space Complexity: O(min(n, m))
        """
        # Initialize variables
        left = 0  # left pointer of the sliding window
        max_length = 0  # maximum length of substring without repeating characters
        char_set = set()  # set to store unique characters in the current window

        # Iterate over the string
        for right in range(len(s)):
            # While the character at the right pointer is in the set, move the left pointer to the right
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the character at the right pointer to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print(s.lengthOfLongestSubstring("bbbbb"))  # Expected: 1
    print(s.lengthOfLongestSubstring("pwwkew"))  # Expected: 3