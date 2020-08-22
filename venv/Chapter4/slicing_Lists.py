# To make a slice, you specify the index of the first and last elements you want to work with.
# To output the first three elements in a list, you would request indices 0 through 3 ,
# which would return elements 0 , 1 , and 2
players = ['Charles', 'Martina', 'Mike', 'Florence', 'Eli']
print(players[0:3])
print(players[1:4])
print(players[2:])
print(players[-3:],"\n")

print('_____LOOPING THROUGH SLICES_____')
# You can use a slice in a for loop if you want to loop through a subset of the elements in a list.
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player,"\n")

print('_____COPYING LISTS_____')
#The code below makes a copy of a list, in this example we use a list of fave foods. Our friend likes the same food.
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My fave foods are")
print(my_foods)

print("\nMy friends fave foods are:")
print(friends_foods,"\n")
#By appending each lists, we add a different food to both lists to prove that they are indeed separate lists.
#Thanks to [:] we can produce two separate lists.
my_foods.append('chicken wings')
friends_foods.append('Tacos')
print(my_foods)
print(friends_foods)
