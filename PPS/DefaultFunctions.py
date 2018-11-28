# Functions
# Default Values - when defining a function a default value is a
# value the function will user for a parameter if the parameter is
# not provided in the function call

def Add(x=5, y=6):
    return x+y
print(Add())
print(Add(12, 13))
print(Add(15))
# Note: Default values must not have standard parameters trailing them.
# Keyword Arguments - In the funtion call you can assign a value to any
# parameter of the function in any order.
def Alarm(h=6, m=30, s=0):
    # Output formatting was used to display trailing 0"s(zero's).
    # Ex: "{1:02d}:{2:02d}"
    print("Wake up! It is {0}:{1:02d}:{2:02d}".format(h, m, s))

# Function calls
Alarm(m=0, s=30, h=4)
Alarm()
Alarm(5)
Alarm(6, 20)
Alarm(7, 30, 45)
