n = int(input("Enter the value of n: " ))

count  = 0 


for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if i ** 2 + j ** 2 == k ** 2:
                count += 1
print(count)