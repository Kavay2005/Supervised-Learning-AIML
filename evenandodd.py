def separate_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

numbers = [4, 7, 1, 8, 3, 12, 15, 23, 28]
even, odd = separate_even_odd(numbers)
print("Even numbers:", even)  # Output: Even numbers: [4, 8, 12, 28]
print("Odd numbers:", odd)  # Output: Odd numbers: [7, 1, 3, 15, 23]
