# If you want to make a list of numbers, you can convert the results of range() directly into a list using the
# list() function.
numbers =list(range(1, 6))
print(numbers)
# output will be [1, 2, 3, 4, 5]

# We can also use the range() function to tell Python to skip numbers in a given range.
# For example, here’s how to list the even numbers between 1 and 10:
even_nums = list(range(2,11,2))
print(even_nums)
#output = [2, 4, 6, 8, 10]
# Same thing below, but odds instead.
odd_nums = list(range(1,12,2))
print(odd_nums)


print("_________________________________________________________________")

#Below is an empty list
squares = []
#Below, we tell Python to loop through each value from 1-10 using range in loop.
for value in range(1, 11):
#Inside the loop(below), th value is raised to the 2nd power and assigned to variable square.
    square = value ** 2
#Here, each new value of square (above), is appended to the list squares.
    squares.append(square)
print(squares)
#output is : [1,   4,    9,    16,   25,   36   49,   64,   81,   100]
#Think of - 1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2


# It can be more concisely written too, by omitting the variable square.
sqrs = []
for value in range(1,11):
    sqrs.append(value**2)
print(sqrs)

# Cubes example:
cubes = []
for value in range(1, 13):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

print("\n")


print("_________________________________________________________________")

print("SIMPLE STATISTICS WITH A LIST OF NUMBERS :)")
#Below is my short list:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#Below the functions min, max, and sum do exactly what you think..
print(min(digits))
# Output as expected - 0
print(max(digits))
# Output is 9
print(sum(digits))
# Total sum of digits in list is- 45

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