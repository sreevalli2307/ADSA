from typing import List

def diagonalBoundarySum(arr: List[List[int]]) -> int:
    n = len(arr)
    total = 0

    # Boundary sum
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                total += arr[i][j]

    # Diagonal sum excluding boundary
    for i in range(1, n - 1):
        # Primary diagonal
        total += arr[i][i]

        # Secondary diagonal
        if i != n - i - 1:
            total += arr[i][n - i - 1]

    return total


if __name__ == '__main__':
    n = int(input())

    mat = []

    for i in range(n):
        mat.append(list(map(int, input().split())))

    print(diagonalBoundarySum(mat))