n = int(input("Enter the value of n = "))
fact = 1
i = n
if(i==0&i==1):
    print(1)
while i>=1:
   
    fact = fact*i
    i= i-1
    
print(fact)    