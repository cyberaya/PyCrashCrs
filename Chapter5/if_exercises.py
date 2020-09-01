#Alien Colors #1:
# Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red'.
# Write an if statement to test whether the alien’s color is green.
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails.
# (The version that fails will have no output.)

#Version that works and produces output:
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('Congrats! You just earned 5 points!')

#Version that fails to produce output:
alien_color = ['green', 'yellow', 'red']
if alien_color is 'green':
    print('Congrats! You just earned 5 points!\n')


#Alien Colors #2:
# Choose a color for an alien as you did in Exercise 5-3, and write an if - else chain.
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

alien_color2 = 'green'
if 'green' in alien_color2:
    print('\nCongrats! You just earned 5 points for shooting the alien!')

else:
    print('Congrats! You just earned 10 points')

alien_color2 = 'red'
if 'green' in alien_color2:
    print('\nCongrats! You just earned 5 points for shooting the alien!')

else:
    print('Congrats! You just earned 10 points')

#Alien Colors #3:
# Turn your if - else chain from Exercise 5-4 into an if - elif -else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien

alien = 'green'
if 'green' in alien:
    print('\nCongrats! You just earned 5 points!')
elif 'yellow' in alien:
    print('Congrats! You just earned 10 points')
elif 'red' in alien:
    print('Congrats! You just earned 15 points')
else:
    print('Sorry, that color is not an option!')

alien = 'yellow'
if 'green' in alien:
    print('\nCongrats! You just earned 5 points!')
elif 'yellow' in alien:
    print('Congrats! You just earned 10 points')
elif 'red' in alien:
    print('Congrats! You just earned 15 points')
else:
    print('Sorry, that color is not an option!')

alien = 'red'
if 'green' in alien:
    print('\nCongrats! You just earned 5 points!')
elif 'yellow' in alien:
    print('Congrats! You just earned 10 points')
elif 'red' in alien:
    print('Congrats! You just earned 15 points')
else:
    print('Sorry, that color is not an option!')
print('\n')


#Stages of Life:
# Write an if - elif - else chain that determines a person’s stage of life.

# Set a value for the variable age , and then:
# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

age = 27

if age <=2:
    print('This is a baby!')
elif age <=4:
    print('This is a toddler!')
elif age <=13:
    print('This is a kid!')
elif age <20:
    print('This is a teenager!')
elif age <=65:
    print('This is an adult!')
elif age <=2:
    print('This is a baby!')
print('\n')

#Favorite Fruit:
# Make a list of your favorite fruits.
# Then write a series of independent if statements that check for certain fruits in your list.
# Make a list of your three favorite fruits and call it favorite_fruits .
# Write five if statements.
# Each should check whether a certain kind of fruit is in your list.
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['strawberry', 'mango', 'pineapple']

if 'strawberry' in favorite_fruits:
    print('You really like', favorite_fruits[0],'!')
if 'grapes' in favorite_fruits:
    print('Adding grapes!')
if 'mango' in favorite_fruits:
    print('You really like', favorite_fruits[1],'!')
if 'kiwi' in favorite_fruits:
    print('Adding kiwi!')
if 'pineapple' in favorite_fruits:
    print('You really like', favorite_fruits[1],'!')
