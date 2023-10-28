"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        input_string = input("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input_string.split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
n = len(numbers)

if n % 2 == 0:
    median = (numbers[n // 2] + numbers[(n // 2) - 1]) / 2
else:
    median = numbers[n // 2]

print("The median of this list is: ", median)
