from typing import List, Optional

class Solution:
    def validParentheses(self, s: str) -> bool:
        """
        Approach: We will use a stack to keep track of the opening parentheses.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Create a dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        # Initialize an empty stack
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracket_map.keys():
                # If the stack is empty or the top of the stack does not match the current closing bracket, return False
                if len(stack) == 0 or stack.pop() != bracket_map[char]:
                    return False
        
        # If the stack is empty after iterating over the entire string, return True; otherwise, return False
        return len(stack) == 0

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.validParentheses("()"))  # Expected: True
    print(s.validParentheses("()[]{}"))  # Expected: True
    print(s.validParentheses("(]"))  # Expected: False
    print(s.validParentheses("([)]"))  # Expected: False
    print(s.validParentheses("{[]}"))  # Expected: True