from typing import List, Optional

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Approach: This problem can be solved by using dynamic programming to build a 2D table where each cell [i][j] represents whether the first i characters of string s match the first j characters of pattern p.
        Time Complexity: O(n*m)
        Space Complexity: O(n*m)
        """
        # Initialize a 2D table with zeros
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # An empty pattern matches an empty string
        dp[0][0] = True
        
        # If the pattern starts with '*', it can match zero characters in the string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill in the rest of the table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
        
        # The answer is in the bottom right cell of the table
        return dp[len(s)][len(p)]

# --- Test Cases ---
if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a")) 
    print(s.isMatch("aa", ".a")) 
    print(s.isMatch("ab", ".*")) 
    print(s.isMatch("aab", "c*a*b")) 
    print(s.isMatch("", "")) 
    print(s.isMatch("aaa", "a.a"))