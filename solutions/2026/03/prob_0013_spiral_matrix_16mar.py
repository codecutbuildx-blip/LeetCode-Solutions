from typing import List, Optional

class Solution:
    def spiralMatrixIII(self, row: int, col: int, rOffset: int, cOffset: int) -> List[List[int]]:
        res = [[0 for _ in range(5)] for _ in range(5)]
        m, n = 5, 5
        cur_row, cur_col = row, col
        dir_x, dir_y = [1, -1][rOffset], [1, -1][cOffset]
        
        while res[cur_row][cur_col] == 0:
            res[cur_row][cur_col] = m*n + 1
            next_row, next_col = cur_row + dir_x, cur_col + dir_y
            
            if (next_row < 0 or next_row >= m) or (next_col < 0 or next_col >= n):
                break
            elif res[next_row][next_col] == 0:
                cur_row += dir_x
                cur_col += dir_y
            else:
                dir_x, dir_y = -dir_x, -dir_y
                cur_row += dir_x
                cur_col += dir_y
        
        return res

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(3, 2, 1, 1))  # Expected: [[16, 3, 10, 11, 12], [15, 14, 9, 5, 7], [13, 4, 8, 2, 6], [12, 1, 5, 3, 11]]
    print(s.spiralMatrixIII(3, 2, -1, -1))  # Expected: [[16, 15, 14, 13, 12], [17, 10, 9, 8, 7], [18, 5, 4, 3, 6], [19, 11, 2, 1, 11]]