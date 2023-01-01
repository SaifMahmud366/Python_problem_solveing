n = int(input("Enter Number You Wanna check = "))

i = 2
while i<=n:
    if n%i == 0:
        break
    i += 1
if i == n:
    print("It's Prime Number!")
else:
    print("It's Not Prime Number!")