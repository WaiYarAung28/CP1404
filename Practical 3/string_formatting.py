"""
CP1404- Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
github -- https://github.com/WaiYarAung28/CP1404
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035
#Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!
print(f"{year} {name} for about ${cost:,}!")

# Using a for loop with the range function and string formatting,
# produce the following right-aligned output (DO NOT use a list):
#   0
#  50
# 100
# 150
numbers = [0, 50, 100, 150]
for i, number in enumerate(numbers, 1):
    print(f"{number}")