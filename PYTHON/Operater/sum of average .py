# Find Sum and Avg of user input list

# Accept a list of numbers from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
# numbers = [int(x) for x in user_input.split()]
# numbers=user_input.split(int())
numbers=0
for x in user_input:
    x.split(int(x))

# Calculate the sum of list elements
total = sum(numbers)

# Find the number of elements in the list
num_elements = len(numbers)

# Calculate the average
if num_elements != 0:
    average = total / num_elements
    print("Sum of list elements:", total)
    print("Average of list elements:", average)
else:
    print("Cannot calculate the sum and average of an empty list.")
