m, n = list(map(int, input("Entr the m and n: ").split()))

matrix = [list(map(int, input("Enter the matrix: ").split())) for _ in range(m)]

combine_matrix = []


for row in matrix:
    for numbers in row:
        combine_matrix.append(numbers)
print(combine_matrix)

combine_matrix.sort()



index = 0


for _ in range(m):
    row_numbers =  combine_matrix[index:index + n]
    print(" ".join(map(str, row_numbers)))
    index += n 











