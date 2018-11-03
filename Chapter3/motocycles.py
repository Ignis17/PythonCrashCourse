# Original Version
motorcyles = ["honda", "yamaha", "suzuki"]
print(motorcyles)

# Modified Version 1.0
motorcyles[0] = "ducati"
print(motorcyles)

# Modified Version 1.1
motorcyles.append("ducati")
print(motorcyles)

# Modified Version 1.2
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Modified Version 1.3
motorcyles.insert(0,"ducati")
print(motorcyles)

# Modified Version 1.4
del motorcyles[0]
print(motorcyles)
del motorcyles[1]
print(motorcyles)

# Modified Version 1.5
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Modified Version 1.6
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Modified Version 1.7 - Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Modified Version 1.8 - Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Modified Version 1.9
"""
Note: The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop to
determine if all occurrences of the value have been removed.
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
