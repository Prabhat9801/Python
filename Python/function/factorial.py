def fact(a):
    k=1
    if (a==0 & a==1):
        print(1)
    for i in range(a,0,-1):
        k = k*i
    print(k)    
            
n = int(input("Enter the value of n = "))
fact(n)
