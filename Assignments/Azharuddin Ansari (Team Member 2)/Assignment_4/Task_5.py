#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
my_list = [8, 2, 3, 0, 7]
result = sum_list(my_list)
print("Sum:", result)
