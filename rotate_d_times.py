list_num = list(map(int, input("Enter the list items: ").split(',')))
f = int(input("Enter the rotation frequency: "))

length = len(list_num)

rotation_frequency = f  % length




rotation_part = list_num[:rotation_frequency]

remaining_part = list_num[rotation_frequency:]

remaining_part.extend(rotation_part)
print(remaining_part)
