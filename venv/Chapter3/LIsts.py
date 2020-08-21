# A list is a collection of items in a particular order. You can make a list that
# includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family.

# In Python, square brackets ( [] ) indicate a list, and individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Lists are ordered collections, so you can access any element in a list by telling Python the index (position).
print (bicycles[2])

print("\n")


dogs = ['GoldenDoodle', 'German Shepherd', 'Lab', 'Dalmatian']
print(dogs[0].title())
print(dogs[0-1].title())
print(dogs[2].title())
print(dogs[1])
print("\n")
print("_________________________________________________________________________________________")
print("By asking for the item at index -1 , Python always returns the last item in the list:")
print(dogs[-1])
#This syntax is quite useful,because you’ll often want to access the last items in a list without knowing exactly how
#long the list is.
#The index - 2 returns the second item from the end of the list,
#The index - 3 returns the third item from the end, and so forth.
doggo = "Winston"
message = f"My first dog as a homeowner was a {dogs[0].title()}. His name is {doggo}."
print (message)

print("_________________________________________________________________________________________")

print('"Short Exercises"')
#Store the names of a few of your friends in a list called names . Print each person’s name by accessing each element in the list, one at a time.")
friends = ['Hector', 'Adrian', 'Cris']
print(friends[0])
print(friends[1])
print(friends[2])
#Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message personalized with the person's name.
print(f"Hello! {friends[0]}")
print(f"Hello! {friends[1]}")
print(f"Hello! {friends[2]}")

#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars = ['Lambo', 'Ferrari', 'Bugatti']
print (f"I've always wished to get a ride in a {cars[2]}. Even more so I'd love to at least own a {cars[0]} Someday.")