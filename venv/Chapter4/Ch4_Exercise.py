

#______________EXERCISES__________________
# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
twenty = list(range(1,21))
for digits in twenty:
    print(digits)


# One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
millions =list(range(1,1_000_001))
for mils in millions:
    print(mils)
print("\n")


# Summing a Million:
# Make a list of the numbers from one to one million
# Then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.
sum_ova_million = list(range(1, 1_000_001))
print("This is the smallest number in the list.")
print(min(sum_ova_million),"\n")
print("This is the largest number in the list.")
print(max(sum_ova_million),"\n")
print("This is the total sum of the list.")
print(sum(sum_ova_million),"\n")

# Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
odd_numbers = list(range(1, 21, 2))
for odds in odd_numbers:
    print(odds)