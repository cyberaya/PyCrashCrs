# Python provides a number of different ways to organize your lists, depending on the situation.
print("__________________________________________________________________________")
print("SORTING A LIST PERMANENTLY WITH THE SORT() METHOD")
#The sort () method will automatically alphabetize the list, and we can no longer revert to the original list.
cars = ['bmw', 'audi', 'mercedes', 'tesla']
cars.sort()
print(cars)

# But you can also sort() in reverse like such.
cars.sort(reverse=True)
print(cars)

print("_________________________________________________________________________")

# You may also temporarily sort the list with sorted() Function.
print("Here is the original list:")
print (cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# Notice that the list still exists in its original order at x after the sorted() function has been used.
print("_________________________________________________________________________")

print("You can also reverse the original order of a list, by using reverse() method. Will not be alphabetically.")
print(cars)
cars.reverse()
print(cars)
# The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by
# applying reverse() to the same list a second time.
print("_________________________________________________________________________")

print("You can find the length of a list by using the len () function.")
brands = ['Nike', 'Adidas', 'Under Armour', 'Reebok']
print(brands)
print(len(brands))

