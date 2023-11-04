def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Sample list
sample_list = [8, 2, 3, 0, 7]

# Calculate the sum
result = sum_numbers(sample_list)

# Print the result
print("Sum of numbers in the list:", result)
