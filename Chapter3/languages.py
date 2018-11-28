lang = []
lang.append("Spanish")
lang.insert(0, "English")
lang.append("French")
lang.insert(int((len(lang)/2)), "Creole")
print(lang)
lang.pop()
print(lang)
del lang[0]
print(lang)
lang.remove("Spanish")
print(lang)
lang.pop()
print(lang)
# print(lang[-1])

"""
Note: If an index error occurs and you can’t figure out how to resolve it, try printing your
list or just printing the length of your list. Your list might look much different than
you thought it did, especially if it has been managed dynamically by your program.
Seeing the actual list, or the exact number of items in your list, can help you sort out
such logical errors.
"""
