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

# *** Doing Something After a for Loop ***
# What happens once a for loop has finished executing?
# Usually, you’ll want to summarize a block of output or move on to other
# work that your program must accomplish.
# Any lines of code after the for loop that are not indented are executed
# once without repetition.

# *** Avoiding Indentation Errors ***
# Python uses indentation to determine when one line of code is connected
# to the line above it.

# *** Forgetting to Indent ***
# Always indent the line after the for statement in a loop.
# If you forget, Python will remind you: Example:
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# *** Forgetting to Indent Additional Lines ***
# Sometimes your loop will run without any errors but won’t produce the
# expected result. This can happen when you’re trying to do several tasks
# in a loop and you forget to indent some of its lines.
