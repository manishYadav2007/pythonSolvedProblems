

password  = input("Enter the valid password: ")

count  = 0 

for each_char in password:
    if each_char.isupper():
        count += 1


if count > 1:
    print("Valid Password")
else:
    print("Invalid Password")
    
    