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

sorted_lst = sorted(numbers)
list_len = len(numbers)
median = 0
index = (list_len - 1) // 2
if len(numbers) % 2 == 0:
    median = (sorted_lst[index] + sorted_lst[index + 1])/2
else:
    median = sorted_lst[index]
print(median)
