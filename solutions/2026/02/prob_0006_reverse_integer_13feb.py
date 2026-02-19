from typing import List, Optional

class Solution:
    def reverseInteger(self, x: int) -> int:
        """
        Approach: We will use a while loop to repeatedly remove digits from the end of the number and add them to the front.
        Time Complexity: O(log|x|), where |x| is the absolute value of the input number
        Space Complexity: O(1), as we only need a constant amount of space to store our variables
        """
        # Check if the input number is negative, in which case we will convert it to positive and remember that it was originally negative
        sign = -1 if x < 0 else 1
        x *= sign

        # Initialize our result variable to 0
        result = 0

        # We will keep removing digits from the end of the number until there are no more digits left
        while x > 0:
            # Get the last digit of the number by taking the remainder when divided by 10
            digit = x % 10
            # Remove the last digit from the number by performing integer division by 10
            x //= 10

            # Add the last digit to our result, but only if it doesn't cause an overflow
            if (result > 2**31 - 1 // 10) or (result == 2**31 - 1 // 10 && digit > 7):
                return 0
            result = result * 10 + digit

        # If the original number was negative, we will convert our result back to a negative number
        return sign * result

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.reverseInteger(123))  # Expected: 321
    print(s.reverseInteger(-456))  # Expected: -654