n = int(input("Enter Factorial Number = "))

fact = 1
i=1
while i<=n:
    fact = fact * i
    i += 1

print("Factorial = ",fact)