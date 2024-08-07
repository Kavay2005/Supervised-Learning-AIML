def sum_even_odd():
    numbers = input("Enter a list of integers (separated by spaces): ")
    numbers_list = []
    
    for num in numbers.split():
        while True:
            try:
                num_int = int(num)
                numbers_list.append(num_int)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                num = input("Enter the number again: ")
    
    even_sum = 0
    odd_sum = 0
    
    for num in numbers_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return even_sum, odd_sum

even_sum, odd_sum = sum_even_odd()
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
