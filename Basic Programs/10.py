n = int(input("Enter N'th value = "))

a = 0
b = 1

for i in range(n - 1):
    c = a + b
    a = b
    b = c

print(b)
