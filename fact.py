def factorial(n):
    pro=1
    for x in range(1,n+1):
        pro=pro*x
    return pro
y=int(input("Enter a number:"))
print("Factorial=",factorial(y))
