# Joined list
joined_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize an empty list to store even numbers
even_numbers = []

# Iterate through the elements in the joined_list
for number in joined_list:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers in the joined_list:", even_numbers)
