str1 = input("Enter the string one: ")
str2 = input("Enter the string two: ")

result = ""

for word in range(len(str1)):
    if str2.startswith(str1[word:]):
        result += str1[word:]
        break
else:
    result = "No Overlapping" 

print(result)
