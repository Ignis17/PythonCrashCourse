# Author: Joel Turbi
# MadLibs


def MadLibs(person, ex1, verb1, verb2, place, place2, noun, noun2, ex2):
    print("\n\nResults:\n\nWe live on a lake. Today " + person + " tested")
    print("the ice. " + ex1 + " it's frozen! Now I am")
    print("off to " + verb1 + " my skates. I " + verb2)
    print("in the " + place + ", not there. I look in the")
    print(place2 + ", nope not there. I search")
    print("high and low for my ice " + noun)
    print("my " + noun2 + "." + ex2 + " they are there!")
    print("Let's go skating!")


def main():
    print("\t\t*Welcome to MabLibs*\n\n")
    person = input("Enter a name of a person: ")
    ex1 = input("Enter an exclamation: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter a verb: ")
    place = input("Enter a place: ")
    place2 = input("Enter a place: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    ex2 = input("Enter an exclamation: ")
    MadLibs(person, ex1, verb1, verb2, place, place2, noun, noun2, ex2)


main()
