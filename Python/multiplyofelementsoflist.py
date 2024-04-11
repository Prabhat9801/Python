x = []
n = int(input("Enter the size of the list = "))
for i in range(0,n):
    y = int(input())
    x.append(y)
print("The list is = ",x)
pro=1
for i in x:
    pro = pro*i
print("The multiplication of all the elments of the list = ",pro)        
