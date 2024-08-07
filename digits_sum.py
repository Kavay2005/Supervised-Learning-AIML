def sum(i):
    sum=0
    while (i !=0):
        x=i%10
        sum=sum+x
        i=int(i/10)
    return su
n=int(input("Enter a number:"))
print("Sum of all digits is :",sum(n))
        
    
