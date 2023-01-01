p = float(input("Enter Amount = "))
r = float(input("Enter rate = "))
t = int(input("Enter Year/Time = "))

a=p*(1+(r/100))**t
ci=a-p

print("Compound Interest = {:.2f}".format(ci))