def natural(n):
    if(n==0):
        return 0
    
    return natural(n-1) + n
n = int(input("Enter the value of n = "))

print(natural(n))