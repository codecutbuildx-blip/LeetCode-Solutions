from typing import List, Optional

class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Approach: Transpose and Reverse
        Time Complexity: O(n*m)
        Space Complexity: O(1)
        
        The idea is to first transpose the matrix (swap rows with columns) 
        and then reverse each row. This way we achieve a rotation of 90 degrees.
        """
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()
        
        return matrix

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: [[7,4,1],[8,5,2],[9,6,3]]
    print(s.rotate([[1,2],[3,4]]))  # Expected: [[3,1],[4,2]]