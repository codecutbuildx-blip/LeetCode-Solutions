from typing import List, Optional
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: We use a hashmap to store the sorted version of each string as key and its corresponding anagram group as value.
        
        Time Complexity: O(NMlogM) where N is the number of strings and M is the maximum length of a string
        Space Complexity: O(NM) for storing all the anagrams in the hashmap
        """
        # Create a hashmap to store the anagram groups
        anagrams = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters in the string and use it as key
            sorted_s = "".join(sorted(s))
            
            # Add the original string to its corresponding anagram group
            anagrams[sorted_s].append(s)
        
        # Return the values of the hashmap which are the anagram groups
        return list(anagrams.values())

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat","tea","ate"],["tan","atn"],["bat"]]
    print(s.groupAnagrams(["a"]))  # Expected: [["a"]]
    print(s.groupAnagrams(["aa"]))  # Expected: [["aa"]]