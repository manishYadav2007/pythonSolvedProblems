

string  = input("Enter the string: ")


result =  string[0] 

for char in range(1, len(string)):
    each_char = string[char]
    
    if each_char == each_char.upper():
        result += " " + each_char
    else:
        result += each_char 
print(result)



