# Author: Joel Turbi
# Description: Associate function.


# Task 1: Associate function - Dictionary out of two lists.
def associate(list1, list2):
    dic = {}
    for element in list1:
        # Checks if there are more keys than values if so it ignores
        # any extra keys & if there aren't enough
        # keys it ignores the extra values.
        if(list1.index(element) < len(list2)):
            dic[element] = list2[list1.index(element)]
        else:
            break
    return dic

# Task 2: Testing Associate function.
def main():
    keys = ["roses", "violets", "sugar"]
    values = ["red", "blue", "sweet"]
    print(associate(keys, values))


main()
