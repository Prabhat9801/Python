x = []
n = int(input("Enter the size of the list =  "))
for i in range(0,n):
    k = int(input())
    x.append(k)
print("The list = ",x)
for i in x:
     if(i%2==0):
        print("The even numbers are = ",i)
     else:
      print("The odd numbers are = ",i)    