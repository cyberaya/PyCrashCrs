#The ability to modify lists is particularly important when you’re working with a list of users on a website or a list of
#characters in a game. However, sometimes you’ll want to create a list of items that cannot change.
#Tuples allow you to do just that.
#Python refers to values that cannot change as immutable. An immutable list is called a tuple!

#A tuple looks just like a list, except you use parantheses() instead of a bracket[].
#When you define a tuple, you can still access the elements by using each item's index.

#For example, if we have a rectangle that should always remain a certain size,we can ensure the size doesn't change
#by inputting the dimensions into a tuple.

#ex)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#If you want to define a tuple with one element , you need to include a trailing comma:
#example, my_t = (3,)

#Looping through all values in a tuple:
#You can loop ove all the values in a tuple using a for loop, just like with a list.
for dimension in dimensions:
    print(dimensions,'\n')

#Writing over a tuple:
#Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple:
#If we want to change our dimensions we can redefin a tuple:
dimensions2 = (100, 25)
print('Original Dimensions:')
for dime in dimensions2:
    print(dime)

dimensions = (400,200)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


randomTuple = ('never', 'change')
for randd in randomTuple:
    print(randd)
