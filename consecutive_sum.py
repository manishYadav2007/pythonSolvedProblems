
def get_sum_of_con_triangle(list_num): # [1, 2, 3, 4]
    con_sum_list  = [] # store the con sum result 
    end_index = len(list_num) - 1 # loop goes to length of list - 1
    # if list length is 4 so the end index is 4 - 1 = 3  
    for each_index in range(end_index):  # 0 1 2 
        # first iteration = each_index = 0
        # sec iteration = each_index = 1
        # third iteration = each_index = 2
        con_sum = list_num[each_index] + list_num[each_index + 1]
        # con_sum  = list_num[0] + list_num[0 + 1] 
        # list_num[1] + list_num[2] = 3 
        
        # con_sum = list_num[1] + list_num[1 + 1] 
        # con_sum = list_num[1] + list_num[2] = 5
        
        # con_sum = list_num[2] + list_num[2 + 1]
        # con_sum = list_num[2] + list_num[3] = 7
        con_sum_list.append(con_sum)
        # con_sum_list.append([3])
        # con_sum_list.append([3, 5])
        # so the final list is = con_sum_list.append([3, 5, 7])
    return con_sum_list # return [3, 5, 7]



def get_con_sum_triangle(list_num): # [1, 2, 3, 4]
    
    # if list_num length greater than 1 run the while loop 
    
    while len(list_num) > 1: # list length is 4 
        
        # call the get get_sum_of_con_triangle function and pass the list value in this function 
        
        con_sum_list = get_sum_of_con_triangle(list_num) # return list is [3, 5, 7]
        print(con_sum_list) # [3, 5, 7]
        list_num = con_sum_list
        # list_num = [3, 5, 7]


list_num = list(map(int, input("Enter the list input: ").split())) # [1, 2, 3, 4]
print(list_num)


# pass list into the get_con_sum_traingle function 
get_con_sum_triangle(list_num)



