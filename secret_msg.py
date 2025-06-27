string = input("Enter the string: ").lower()

words = string.split()


result = []

for char  in string:
    encoded_string = []
    for word in char:
        if word.isalpha():
            position = ord(word) - ord("a") + 1
            encoded_string.append(str(position))
    result.append("-".join(encoded_string))
    
    
    final_result = " ".join(result)
    
print(final_result)

            
            