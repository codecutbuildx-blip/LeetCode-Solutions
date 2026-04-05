from typing import List, Optional
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: We use a hashmap where the key is the sorted version of each string and the value is a list of anagrams.
        
        Time Complexity: O(NMlogM) where N is the number of strings and M is the maximum length of a string. This is because we are sorting each string, which takes O(MlogM) time.

        Space Complexity: O(NM) where N is the number of strings and M is the maximum length of a string. This is because we are storing all the sorted strings in our hashmap.
        """
        
        # Create a hashmap to store the anagrams
        anagram_map = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters in the string and use it as the key in our hashmap
            sorted_s = "".join(sorted(s))
            
            # Add the original string to the list of values for the corresponding key
            anagram_map[sorted_s].append(s)
        
        # Return a list of all the values in our hashmap (i.e., all the groups of anagrams)
        return list(anagram_map.values())

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Expected: [["eat","tea","ate"],["tan","atn"],["bat"]]
    print(s.groupAnagrams(["a"]))  # Expected: [["a"]]
    print(s.groupAnagrams(["aa"]))  # Expected: [["aa"]]