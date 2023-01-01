n = int(input("Enter Value = "))

temp = n
b = len(str(n))
sum = 0

while n!=0:
    remaind = n % 10
    sum = sum + (remaind**b)
    n = n // 10

if temp == sum:
    print("This is Armstrong Number")
else:
    print("This is not Armstrong Number")