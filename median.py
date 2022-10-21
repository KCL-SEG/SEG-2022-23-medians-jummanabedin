"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
median = 0
if len(numbers) % 2 == 0:
    median = (numbers[len(numbers) - 1] // 2 + numbers[len(numbers)] // 2)/2
else:
    median = numbers[len(numbers) - 1] // 2
print(median)
