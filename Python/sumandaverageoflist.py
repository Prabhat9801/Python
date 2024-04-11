x = []
y = int(input("Enter the size of the list = "))
for i in range(0,y):
    k = int(input())
    x.append(k)
    
print(x)
sum = 0
for z in x:
    sum = sum + z
average = sum / len(x) 
print("Sum = ",sum)
print("Average = ",average)   