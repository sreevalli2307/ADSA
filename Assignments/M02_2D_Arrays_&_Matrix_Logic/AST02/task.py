#Task
from typing import List

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return matrix
        
    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check if the first row contains any zero
    for c in range(n):
        if matrix[0][c] == 0:
            first_row_zero = True
            break

    # Check if the first column contains any zero
    for r in range(m):
        if matrix[r][0] == 0:
            first_col_zero = True
            break

    # Use first row and first col as markers for the rest of the matrix
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Zero out cells based on markers
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # Zero out the first row if needed
    if first_row_zero:
        for c in range(n):
            matrix[0][c] = 0

    # Zero out the first column if needed
    if first_col_zero:
        for r in range(m):
            matrix[r][0] = 0

    return matrix


if __name__ == '__main__':
    matrix = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            row = list(map(int, line.split()))
            matrix.append(row)
        except EOFError:
            break
            
    print(setZeroes(matrix))
