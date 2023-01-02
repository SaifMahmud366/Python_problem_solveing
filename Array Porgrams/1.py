list1=[]
n=(int(input("How many numbers = ")))

i=1
while i<=n:
    list1.append(int(input()))
    i+=1
print("list= ",list1)

# sum = sum(list1)

sum=0
for i in list(list1):
    sum=sum+i

print(sum)