#__________ LIST COMPREHENSIONS____________

# A list comprehension allows you to generate this same list in just one line of code!
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically
# appends each new element.

squares = [value**2 for value in range(1,11)]
print(squares)

# Notice that no colon is used at the end of the for statement.
# The result is the same list of square numbers you saw earlier...

cubes = [value**3 for value in range(1,11)]
print(cubes)

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