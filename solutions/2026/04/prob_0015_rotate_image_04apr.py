def rotate(self, matrix: List[List[int]]) -> None:
    """
    Rotate the given image by 90 degrees clockwise.
    
    Approach: Transpose and reverse each row in the matrix.
    Time Complexity: O(n*m) where n is the number of rows and m is the number of columns.
    Space Complexity: O(1) as we are modifying the input matrix in-place.
    """
    
    # Step 1: Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        # Use Python's slice notation to reverse the row
        row.reverse()