#Create a function with If statement whis is used to find the odd numbers
def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = find_odd_numbers(numbers)
print("Odd numbers in the list:", result)
