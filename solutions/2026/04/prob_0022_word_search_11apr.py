from typing import List, Optional
from collections import defaultdict

class Solution:
    def wordSearch(self, board: List[List[str]], words: List[str]) -> List[Optional[str]]:
        """
        Approach: 
            We use a hash table to store the coordinates of each character in the board.
            Then we iterate through all possible words and check if they exist in the board.

        Time Complexity: O(N*M*4^L), where N is the number of rows, M is the number of columns, L is the length of the word.
        Space Complexity: O(1), as we only use a constant amount of space to store the hash table and other variables.
        """
        # Create a hash table to store the coordinates of each character in the board
        char_coords = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                char_coords[board[i][j]].add((i, j))

        # Iterate through all possible words and check if they exist in the board
        result = []
        for word in words:
            if not self.search(word, 0, 0, char_coords, set()):
                result.append(None)
            else:
                result.append(word)

        return result

    def search(self, word, i, j, char_coords, visited):
        """
        Recursive function to check if a word exists in the board.

        Args:
            word (str): The current word being searched.
            i (int): The current row index.
            j (int): The current column index.
            char_coords (dict): A hash table of character coordinates.
            visited (set): A set of visited cells to avoid infinite loops.

        Returns:
            bool: True if the word exists in the board, False otherwise.
        """
        # If the current cell is out of bounds or has been visited, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visited:
            return False

        # Mark the current cell as visited
        visited.add((i, j))

        # If the current character does not match the first character of the word, return False
        if board[i][j] != word[0]:
            return False

        # If we have checked all characters in the word and they match, return True
        if len(word) == 1:
            return True

        # Recursively search for the remaining characters in the word
        return self.search(word[1:], i + 1, j, char_coords, visited) or \
               self.search(word[1:], i - 1, j, char_coords, visited) or \
               self.search(word[1:], i, j + 1, char_coords, visited) or \
               self.search(word[1:], i, j - 1, char_coords, visited)

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]
    words = ["ABCCED", "SEE"]
    print(s.wordSearch(board, words))  # Expected: ['ABCCED', None]