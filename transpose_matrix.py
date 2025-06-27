

def get_transpose(matrix_row, n, m):
    transpose = []
    for row in range(n):
        row_result = []
        for col in range(m):
            row_result.append(matrix_row[col][row])
        transpose.append(row_result)

n, m = list(map(int, input("Enter the order of matrix: ").split()))
matrix_row = [list(map(int, input("Enter the matrix: ").split())) for i in range(1, n + 1)]
transpose_result = get_transpose(matrix_row, n, m)
for each_row in transpose_result:
    print(each_row)
    
    
    

