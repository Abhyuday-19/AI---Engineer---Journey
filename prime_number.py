def prime_number():
    num=int(input("Enter the number:"))
    count=0
    i=1
    while(i<=num):
        if(num%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print("Number is prime")
    else:
        print("Number is not prime")
prime_number()