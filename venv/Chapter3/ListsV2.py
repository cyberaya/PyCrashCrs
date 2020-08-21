#Changing, Adding, and Removing Elements


print("__________________________________________________________")

print("MODIFYING ELEMENTS IN A LIST")
pizzas = ['Pepperoni', 'Sausage', 'Supreme']
print(pizzas)
#Below is the code to change the value of an element in a list.
pizzas[1] = 'Cheese'
print(pizzas)
#Now it prints cheese in place of sausage.

print("__________________________________________________________")

print("ADDING ELEMENTS TO A LIST")
# The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list,
# the new element is added to the end of the list.
# Use the .append () method.
pizzas.append('Hawaiian')
print(pizzas)
#The list below starts with no elements but by appending, it adds in the values.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("__________________________________________________________")

print("INSERTING ELEMENTS TO ANY POSITION WITHIN A LIST")
animals = ['lion', 'bear', 'zebra']
print(animals)
# You can insert an element to whatever position you like within the list, with the code below.
animals.insert(0,'giraffe')
animals.insert(2, 'Kangaroo')
print(animals)
animals.append('monkey')
print(animals)
print (f"I went to the zoo today and saw a {animals[2]}!")

print("__________________________________________________________")

print("REMOVING ELEMENTS FROM A LIST")
# You can delete a an element from a list by using the del statement.
ice_cream = ['chocolate', 'vanilla', 'mint']
print(ice_cream)
del ice_cream[2]
print(ice_cream)

ice_cream.append('butter pecan')
print(ice_cream)
print(ice_cream[1].title())

print("__________________________________________________________")

# Removing an element using the pop method.
service_branches = ['Marines', 'Navy', 'Army', 'Air Force', 'Coast Guard']
print(service_branches)
#By creating the popped_service_branch, you are essentially assigning the popped branch to a new list of popped branches
popped_service_branch = service_branches.pop()
print(service_branches)
# When you print the popped branch you will now see the last element from the service branch list.
print(popped_service_branch)

print(f"The last service branch I ever thought of joining was {popped_service_branch}.")
# You can also pop from any position within a list.
branch_joined = service_branches.pop(0)
print(f"The service branch I did join was the {branch_joined.upper()}.")
# And as you can see, the list now only prints the elements that were not 'popped'
print(service_branches)

print("__________________________________________________________")

print("REMOVING AN ITEM BY VALUE")
# Sometimes you won't know the position of the value you want to remove from a list, you can use the remove() method.
clothes = ['T-shirt', 'Jeans', 'Shoes', 'Belt']
print(clothes)
clothes.remove('Belt')
print(clothes)

too_expensive = 'Shoes'
clothes.remove(too_expensive)
print(clothes)
print(f"Them Gucci {too_expensive} were just too expensive for my liking.")
