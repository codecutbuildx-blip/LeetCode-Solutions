def wordSearch(board, word):
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or word[index] != board[r][c]:
            return False
        temp, board[r][c] = board[r][c], '/'
        for dr, dc in directions:
            if dfs(r + dr, c + dc, index + 1):
                return True
        board[r][c] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

class Solution:
    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        return wordSearch(board, word)