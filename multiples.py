def print_multiples(num, limit):
    for i in range(num, limit + 1, num):
        print(i)
x=int(input("Enter the number :"))
y=int(input("Enter the limit:"))
print_multiples(x, y)
