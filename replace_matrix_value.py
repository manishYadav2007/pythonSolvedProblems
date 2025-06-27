
def get_new_matrix(matrix, old_value, new_value):
    # store the final result matrix 
    updated_matrix = []
    for row in matrix: # this loop cover all rows in matrix 
        # this will store the individual updated matrix row 
        updated_row = []
        len_of_row = len(row) # take length of individual row 
        for i in range(len_of_row):
            # check if individual row element is equal to target value(old value) which stote the rew value in the updated row  
            if row[i] == old_value:
                updated_row.append(new_value)
            else:
                # if row is not equal to old value run the else block  
                updated_row.append(row[i])
        updated_matrix.append(updated_row)
    return updated_matrix
        



m, n = list(map(int, input("Enter the matrix order: ").split()))
print(m, n)


matrix = [list(map(int, input("Enter the matrix rows: ").split())) for i in range(m)]

old_value, new_value = list(map(int, input("Enter the values which you have replacing that: ").split()))



result = get_new_matrix(matrix, old_value, new_value)
print(result)


for each_row in result:
    print(each_row)

