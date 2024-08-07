def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [4, 7, 1, 8, 3]
print(find_largest(numbers))  # Output: 8
