x = float(input("Enter the value of year = "))
if(x%400==0) and (x%100==0):
    print("This is the leap year")
elif(x%4==0) and (x%100!=0):
    print("This is the leap year")

else :
    print("This is not the leap year")