"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError occur when numerator or denominator entered is non-numeric value likes " %$&* ".
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError occur when denominator is equal to zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   I could change the code to avoid the possibility of a ZeroDivisionError by adding 1 to denominator when denominator
   is entered zero.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
    else:
        fraction = numerator / (denominator + 1)
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")