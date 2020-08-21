# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting  them to dinner.

dinner_guests = ['Elon Musk', 'Brad Pitt', 'Drake', 'Bad Bunny']
print(f"Hello {dinner_guests[0]}, you are cordially invited to have dinner with Mr. Raya.")
print(f"Hello {dinner_guests[1]}, you are invited over to Mr. Raya's for dinner this evening.")
print(f"Hello {dinner_guests[2]}, thank you for accepting the dinner invitation at Mr. Raya's")

print("__________________________________________________________________________________________________")

# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite. Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
print(f"Ladies and gentlemen, please see our guests list for tonight's dinner:", dinner_guests)

print(f"\tWe regret to inform our guests that Mr. {dinner_guests[3]} unfortunately cannot make it to the dinner tonight.")

dinner_guests[3] = 'Keanu Reeves'
print(f"Please see our updated list of guests:", dinner_guests)

print(f"Thank you for accepting the invitation so late Mr.", dinner_guests[3])

