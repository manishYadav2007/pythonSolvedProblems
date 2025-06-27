a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

max_num = max(a, b)

range_value = a * b 


for num in range(max_num, range_value + 1):
    if num % a ==  0 and num % b == 0:
        lcm = num 
        break 
print(lcm)
