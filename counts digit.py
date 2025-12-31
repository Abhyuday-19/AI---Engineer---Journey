Number_1=int(input("Enter the number:"))
if Number_1==0:
    print("Number of digit is : 1")
else:
    count=0
    while Number_1>0:
       count=count+1
       Number_1=Number_1//10
    print("Number of digit is :",count)