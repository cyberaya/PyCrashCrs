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


millions =list(range(1,1_000_001))
for mils in millions:
    print(mils)


