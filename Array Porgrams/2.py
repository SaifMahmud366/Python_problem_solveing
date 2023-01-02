list1=[]
n=(int(input("How many numbers = ")))

i=1
while i<=n:
    list1.append(int(input()))
    i+=1

print("Lrgest Number = ",max(list1))