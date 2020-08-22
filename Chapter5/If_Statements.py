print('CHAPTER 5!\n')
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print(cars, '\n')

# CONDITIONAL TESTS
# At the heart of every if statement is an expression that can be evaluated as True or False, called a conditional test.
# Python uses the values True and False to decide whether the code in an if statement should be executed.
# If a conditional test evaluates to True , Python executes the code following the if statement.
# If the test evaluates to False , Python ignores the code following the if statement.

car = 'Audi'
car == 'audi'
print(car)

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!!\n')

answer = 17
if answer != 42:
    print('That is not the correct answer, Try again!')

# You can include various mathematical comparisons in your conditional statements as well
# Such as less than, less than or equal to, greater than, and greater than or equal to:

age = 19
if age < 21:
    print(True)
if age <= 21:
    print(True)
if age > 21:
    print(False)
if age >= 21:
    print(False)

