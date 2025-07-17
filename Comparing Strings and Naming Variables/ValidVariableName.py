

variable_name = input("Enter the variable name: ")

is_valid = True 

for char in variable_name:
    unicode_value = ord(char)
    
    upper_case = (65 <= unicode_value and 90 >= unicode_value)
    lower_case = (97 <= unicode_value and 122 >= unicode_value)
    digits = (48 <= unicode_value and 57 >= unicode_value)
    
    valid_char = upper_case or lower_case or digits 
    
    if not valid_char:
        is_valid = False 
        break 

print(is_valid)




    
    