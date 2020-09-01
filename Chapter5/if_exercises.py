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