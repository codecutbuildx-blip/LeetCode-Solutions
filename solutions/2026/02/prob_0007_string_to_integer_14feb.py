from typing import List, Optional

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Approach: This problem can be solved by first removing any leading whitespace from the string.
        We then check if the resulting string is empty and return 0 in this case. Next, we try to parse
        the integer value from the string. If the string starts with a negative sign, we remove it and
        adjust our target sum accordingly. If the string contains any non-numeric characters, we stop
        parsing at that point.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Remove leading whitespace
        s = s.lstrip()
        
        # Check if string is empty and return 0
        if not s:
            return 0
        
        # Initialize target sum to 0
        target_sum = 0
        
        # Check for negative sign
        if s[0] == '-':
            # Remove negative sign and adjust target sum
            s = s[1:]
            target_sum = -target_sum
        elif s[0] == '+':
            # Remove positive sign
            s = s[1:]
        
        # Parse integer value from string
        for char in s:
            if not char.isdigit():
                break
            target_sum = target_sum * 10 + int(char)
        
        return target_sum

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))  # Expected: 42
    print(s.myAtoi("-42"))  # Expected: -42
    print(s.myAtoi("4193 with words"))  # Expected: 4193
    print(s.myAtoi("words and 987"))  # Expected: 0