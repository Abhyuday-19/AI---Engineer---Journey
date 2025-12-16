Name=input("Enter the name of student:")
print(Name,"is a good student")
Marks=int(input("Enter the marks of student:"))
if(Marks>=90):
    print("You got grade A")
elif(Marks<80 and Marks>=80):
    print("You got grade B")
elif(Marks==50 and Marks>=50):
    print("Tou got grade C")
else:
    print("You are fail")