n=int(input("enter a number:"))
if n<=1:
    print("not prime")
else:

    for i in range(2,n):

        if n % 2 == 0:
            print("not prime")
            break
        else:
            print("its is prime")
