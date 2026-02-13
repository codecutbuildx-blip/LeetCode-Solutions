from typing import List, Optional

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Approach: Convert integer to string and compare with its reverse.
        Time Complexity: O(n), where n is the number of digits in the integer.
        Space Complexity: O(n), for the string representation.
        """
        # Convert integer to string
        str_x = str(x)
        
        # Compare string with its reverse
        return str_x == str_x[::-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))  # Expected: True
    print(s.isPalindrome(-121))   # Expected: False