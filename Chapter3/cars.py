# Sorting a List Permanently with the sort() Method
cars = ["bmw", "audi", "toyota", "subaru"]
original = cars
cars.sort()
print(cars)
#The sort() method,as shown above, changes the order of the list permanently.

# Modified Version 1.1
'''
You can also sort this list in reverse alphabetical order by passing the
argument reverse=True to the sort() method. The following example sorts
the list of cars in reverse alphabetical order:
'''
cars.sort(reverse=True)
print(cars)

# Modified Version 1.2
# Sorting a List Temporarily with the sorted() Function
print("Here is the original list:")
print(original)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print()

'''
Note: Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase. There are several ways to interpret capital letters when you’re deciding on
a sort order, and specifying the exact order can be more complex than we want to deal
with at this time. However, most approaches to sorting will build directly on what you
learned in this section.
'''

# Modified Version 1.3
# Printing a List in Reverse Order
print(cars)
cars.reverse()
print(cars)
'''
The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time.
'''

# Modified Version 1.4
# Finding the Length of a List
print(len(cars))
'''
Python counts the items in a list starting with one, so you shouldn’t run into any off-
by-one errors when determining the length of a list.
'''
