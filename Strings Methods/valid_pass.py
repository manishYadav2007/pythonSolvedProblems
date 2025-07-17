password = input("Enter the password: ")

count = 0 

for each_char in password:
    if each_char.isdigit():
        count += 1 

if count  > 0 :
    print("Valid Password")
else:
    print("Invalid Password")


