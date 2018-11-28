a = "Hello World!"
b = "Hi"*3
c = "Whatever you want"
d = "1 is an odd number"

# capitalize()- makes the first letter it encounters and capitalizes it.
# while leaving the rest of the letters lower-case.
print(a.capitalize()) # Output: "Hello world!"

# count() - returns the count of all the occurrances of the substring parameter.
print(b.count("Hi")) # Output: 3

# find() - returns the index of the first occurrance of the substring parameter.
# If the substring is not present it returns -1.
print(c.find("you")) # Output: 9
print("free".find("you")) # Output: -1

# lower() - returns a copy of the string with all the letters lower-case.
print(b.lower()) # Output: "hihihi"

# upper() - returns a copy of the string with all the letters upper-case.
print(b.upper()) # Output: "HIHIHI"

# replace() - returns a copy of the string with all the occurrances of the old
# substring replaced with the new substring.
print(c.replace("you","she")) # Output: "Whatever she want"

# strip() - returns a copy og the string with all characters in the parameter removed
# from the front and back of the string. If no parameter is provided , it removes whitespaces.
print ("slips".strip('s')) # Output: lip
print (" Heat ".strip()) # Output: "Heat"

# split() - returns a list of substrings of the string divided by the delimiter parameter.
print (c.split()) # Output: ['Whatever','you','want']
