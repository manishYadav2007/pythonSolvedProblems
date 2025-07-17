string  = input("Enter the string: ").lower()

is_palindrome = False 

reversed_str = string[::-1]

if reversed_str == string:
    is_palindrome = True 
else:
    is_palindrome = False 

print(is_palindrome)


