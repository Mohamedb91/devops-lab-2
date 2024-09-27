# average.py

# Prompt the user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ").split()

# Convert the input strings to floats
numbers = [float(num) for num in numbers]

# Calculate the average
average = sum(numbers) / len(numbers)

# Find the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Print the results
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
