# CS310 Assessment 1
# Joel Turbi
# Prints out * 5 times in descending order.
def Message():
    symb = "*"
    num = int(input("Enter a number:"))
    for i in range(num,0,-1):
        print("*"*i)
Message()
