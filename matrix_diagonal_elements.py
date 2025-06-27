def get_diagonal_matrix(matrix, n, m):
    diagonal_row = []
    for row in range(n):
        if row < m:
            diagonal_row.append(matrix[row][row])
    return diagonal_row

n, m = list(map(int, input("Enter the matrix order: ").split()))
matrix = [list(map(int, input("Enter the matrix input: ").split())) for i in range(n)]
diagonal_elements = get_diagonal_matrix(matrix, n, m)
print(diagonal_elements)








