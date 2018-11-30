squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)
print("Powers of 2 from 1-10:\n",*squares)

### NOTE ###
# The examples in this section use short lists of numbers in order to fit
# easily on the page. They would work just as well if your list contained
# a million or more numbers.
