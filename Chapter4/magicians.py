# Original Version
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)
for magician in magicians:
    # Modified Version 1.0
    print(magician.title() + ", that was a great trick!")
    # Modified Version 1.1
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone. That was a great magic show!")
