# INTEGERS

# You can add ( + ), subtract ( - ), multiply ( * ), and divide ( / ) integers in Python.

print(2 + 3)

print(3 - 2)

print(2 * 3)

print(3 / 2)

print("\n")

# Python uses two multiplication symbols to represent exponents:
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)
print("\n")

# Python supports the order of operations too, so you can use multiple operations in one expression.")
print(2 + 3 * 4)
print((2 + 3) * 4)

print("\n")

# _______________________________________________________________________________________________

# FLOATS

# Python calls any number with a decimal point a float.
print(0.1 + 0.1)
print(0.2 + 0.2)
print(0.2 * 0.1)
print(2 * 0.2)

print("\n")

# When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float:

print(4 / 2)

# If you mix an integer and a float in any other operation, you’ll get a float as well:
print(1 + 2.0)

# Python defaults to a float in any operation that uses a float, even if the output is a whole number.
print("\n")

# When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:
universe_age = 14_000_000_000
print(universe_age)

# You can assign values to more than one variable using just a single line
x, y, z = 0, 0, 0
angel, adrian, hector = 27, 22, 24
print(angel)
print(adrian)
print(hector)

# A constant is like a variable whose value stays the same throughout the life of a program.
MAX_CONNECTIONS = 5000
