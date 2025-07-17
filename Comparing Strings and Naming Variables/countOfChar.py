string  = input("Enter the string value: ")
ascii_value = int(input("Enter the ascii value: "))

count = 0 


for i in string:
    if ord(i) == ascii_value:
        count += 1
print(count)

