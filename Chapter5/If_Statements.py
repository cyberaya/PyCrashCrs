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
#To check whether two conditions are both True simultaneously, use the keyword -and- to combine the 2 conditional tests.
age = 19
if age < 21:
    print(True)
if age <= 21:
    print(True)
if age > 21:
    print(False)
if age >= 21:
    print(False)

print('\n')
age_0 = 22
age_1 = 18
if age_0 >=21 and age_1 >= 21:
    print(True)
else:
    print(False)

#An or expression onyl fails when both individual tests fail. See example below:
age_2 = 18
age_3 = 18
if age_2 >= 21 or age_3 >=21:
    print(True)
else:
    print(False)

#in this example the test outputs as True because age_3 passes the test.
age_2 = 18
age_3 = 24
if age_2 >= 21 or age_3 >=21:
    print(True)
else:
    print(False,'\n')

print('\nCHECKING TO SEE WHETEHER A VALUE IS IN A LIST_________________')
#The technique below using in is useful because you can test to check if the value pepperoni already exists in the list.
requested_toppings = ['mushrooms', 'onions', 'pineapples']
if 'mushrooms' in requested_toppings:
    print(True)

if 'pepperoni' in requested_toppings:
    print(False)

print('\nCHECKING TO SEE WHETEHER A VALUE IS NOT IN A LIST_________________')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f'{user.title()} is not banned...')
