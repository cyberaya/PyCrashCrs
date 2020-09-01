print('Using if Statements with Lists'.upper(),'\n')

#Checking for Special Items:

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('Finished making your pizza!\n')


# What if the pizzeria runs out of green peppers?
# An if statement inside the for loop can handle this situation appropriately:

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, but we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')