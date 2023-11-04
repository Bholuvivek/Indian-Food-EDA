def find_odd_numbers(input_list):
    # Initialize an empty list to store odd numbers
    odd_numbers = []
    
    # Iterate through the elements in the input_list
    for number in input_list:
        if number % 2 != 0:
            odd_numbers.append(number)
    
    return odd_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = find_odd_numbers(my_list)
print("Odd numbers in the list:", result)
