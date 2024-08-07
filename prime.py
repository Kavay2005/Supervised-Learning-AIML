def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print("Given number is not a prime number.")
            break

    else:
            return 1
num=int(input("Enter a number:"))
x=is_prime(num)
if x==1:
    print("Given number is a prime number")
            
        
