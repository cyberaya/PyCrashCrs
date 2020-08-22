#Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#Print the message - The first three items in the list are:.
#Then use a slice to print the first three items from that program’s list.

#Print the message Three items from the middle of the list are:. Use a slice to
#print three items from the middle of the list.

#Print the message The last three items in the list are:.
#Use a slice to print the last three items in the list.

#1
print('The first 3 items in the list are:')
books = ['Python Crash Course', 'Learn Linux', 'The CdC', 'Cybersecurity and Cyberwar', 'Automate the Boring Stuff']
print(books[:3],'\n')

#2
print('The 3 items from the middle of the list are:')
books = ['Python Crash Course', 'Learn Linux', 'The CdC', 'Cybersecurity and Cyberwar', 'Automate the Boring Stuff']
print(books[1:4],'\n')

#3
print('The last 3 items in the list are:')
books = ['Python Crash Course', 'Learn Linux', 'The CdC', 'Cybersecurity and Cyberwar', 'Automate the Boring Stuff']
print(books[2:],'\n')

#Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas .
#Then, do the following: Add a new pizza to the original list.

#Add a different pizza to the list friend_pizzas .
#Prove that you have two separate lists.

#Print the message - My favorite pizzas are:, and then use a for loop to print the first list.
#Print the message - My friend’s favorite pizzas are:, and then use a for loop to print the second list.
#Make sure each new pizza is stored in the appropriate list.

my_pizzas = ['cheese','pepperoni','sausage']
friends_pizzas = my_pizzas[:]

print('My favorite pizzas are:')
my_pizzas.append('Supreme')
print(my_pizzas,'\n')

print('My friends favorite pizzas are:')
friends_pizzas.append('Hawaiian')
print(friends_pizzas,'\n')


print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print('\n')
print('My friend’s favorite pizzas are:')
for friend_faves in friends_pizzas:
    print(friend_faves)

