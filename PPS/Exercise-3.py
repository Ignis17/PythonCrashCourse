# Author: Joel Turbi
# Description: Prints song to screen

def song(i):
    print(str(i) + " little monkeys jumping on the bed")
    print("One fell down and bump his head")
    print("Mama called the doctor and the doctor said")
    print("No more monkeys jumping on the bed.\n")

def main():
    for i in range(5, 1, -1):
        song(i)
    print("1" + " little monkey jumping on the bed")
    print("One fell down and bump his head")
    print("Mama called the doctor and the doctor said")
    print("No more monkeys jumping on the bed.")

main()
