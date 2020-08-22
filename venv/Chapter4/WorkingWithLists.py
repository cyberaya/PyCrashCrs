print("LOOPING THROUGH AN ENTIRE LIST...")

# Using a for loop
magicians = ['alice', 'david', 'carolina']
# The line below tells Python to pull a name from the list  magicians , and associate it with the variable magician .
for magician in magicians:
    #print(magician)

# It might help to read this code as “For every magician in the list of magicians, print the magician’s name.”
# The output is a simple printout of each name in the list:
# The concept of looping is important because it’s one of the most common ways a computer automates repetitive tasks.
# keep in mind when writing your own for loops that you can choose any name you want for the temporary variable that
# will be associated with each value in the list

    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

print("_________________________________________________________________________")

programs = ['Python', 'Java', 'NodeJS', 'C++']
for program in programs:
        print(program)
        print(f"I really enjoy coding in {program}!\n")
print("I really love programing!")
print("_________________________________________________________________________")

operating_systems = ['Linux', 'Windows', 'MacOS']
for os in operating_systems:
    print(os)
    print(f"I have become more and more proficient with {os} as the years pass by.\n")
print("But I still like Linux the best!\n")


randomList = ['item1', 'item2']
for randoms in randomList:
    print(randoms)