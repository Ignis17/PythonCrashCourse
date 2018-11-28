def SmallestNumber(x,y,z):
    least = x

    if y < least:
        least = y
    if z < least:
        least = z
    return least

result = SmallestNumber(3,65,1)
print ("The smallest number is: ",result)
