
string = input("Enter the string: ")

result = string[0]

for char in range(1, len(string)):
    
    if string[char] == string[char].upper():
        result += "-" + string[char].lower()
    else:
        result += string[char].lower()
    

print(result)

