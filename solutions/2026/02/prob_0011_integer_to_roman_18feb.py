from typing import List, Optional

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Approach: We use a dictionary to map Roman numerals to their integer values.
        Then we iterate over the dictionary in descending order of value and subtract
        the current value from the number as many times as possible. The corresponding
        Roman numeral is added to the result string each time.
        Time Complexity: O(1) because we are using a fixed-size dictionary
        Space Complexity: O(1) because we are not using any data structure that scales with input size
        """
        # Define a dictionary mapping Roman numerals to their integer values
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        
        # Initialize an empty string to store the result
        result = ''
        
        # Iterate over the dictionary in descending order of value
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            # Subtract the current value from the number as many times as possible
            while num >= value:
                num -= value
                # Add the corresponding Roman numeral to the result string
                result += numeral
        
        return result

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3))  # Expected: III
    print(s.intToRoman(4))  # Expected: IV
    print(s.intToRoman(9))  # Expected: IX
    print(s.intToRoman(13))  # Expected: XIII
    print(s.intToRoman(44))  # Expected: XLIV
    print(s.intToRoman(1000))  # Expected: M