string = input("Enter the string: ").lower()

words = string.split()
result = []


for word in words:
    encoded = []
    for char in word:
        if char.isalpha():
            position = ord(char) - ord("a") + 1 
            encoded.append(str(position))
    result.append("_".join(encoded))
    
    final_output = " ".join(result)

print(final_output)




