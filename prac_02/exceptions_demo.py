"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

    ValueError occurs when the input for numerator
    and denominator is not digit such as 'a' or '$'.

2. When will a ZeroDivisionError occur?

    ZeroDivisionError occurs when 0 is inputted as denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (except 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
