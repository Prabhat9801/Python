def fact(a):
    if(a==0 | a==1):
        return 1
    else :
        return fact(a-1)*a
n = int(input("Enter the valuwe of n = "))
print(fact(n))

     