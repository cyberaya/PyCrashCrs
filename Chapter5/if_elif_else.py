print('THE IF-ELIF-ELSE CHAIN\n')

#Often you'll need to test more than two possible situations.
#To evaluate more than one coniditional test you can use the if-elif-else chain.
#Runs conditional tests in order until one passes.
#When a test passes and executes, it skips the rest of the tests

#Many real-world situations involve more than two possible conditions.
#For example, consider an amusement park that charges different rates for different age groups:

#Admission for anyone under age 4 is free.
#Admission for anyone between the ages of 4 and 18 is $25.
#Admission for anyone age 18 or older is $40.

#The following code tests for the age group of a person and then prints an admission price message:

age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age <18:
    print('Your admission is $25.')
else:
    print('Your admission cost is $40.')

#Another example, with more elif blocks:

age = 21
if age <18:
    price = 150
elif age >= 21:
    price = 100

elif age >=50:
    price = 50
else:
    price = 75
print(f'\nThe price for your monthly insurance is ${price}.')





