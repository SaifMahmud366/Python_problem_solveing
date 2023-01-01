import math

n=int(input("Enter Your Number = "))

a1=(5*(n**2))+4
a2=(5*(n**2))-4
b1=math.sqrt(a1)
b2=math.sqrt(a2)

if ((b1)**2 == a1) or ((b2)**2 == a2):
    print("{} is fibonacci number !".format(n))
else:
    print("{} is not fibonacci number.".format(n))