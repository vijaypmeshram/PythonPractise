# funny games is about jumbling of names
# you have take number of a person
# then enter the names
# jumbled names and surname

import random
last_name = []
first_name = []
def breakk(name):
    name1 = name.split(" ")
    for i in name1[:-1]:
        first_name.append(i)
    for i in name1[1:]:
        last_name.append(i)
    # print(first_name, last_name)
    return first_name, last_name

def addingname():
    names = []
    n = int(input("Enter the number of a person: \n"))
    for i in range(n):
        name = input("Enter the name: \n")
        names.append(name)
# namelist = [breakk(name) for name in names]
    return names



if __name__ == '__main__':
    namelist = addingname()
    # print(namelist)
    for i in namelist:
        breakk(i)
    # print(first_name, last_name)
    print("here list of your new names")
    for item1 in first_name:
        for item2 in last_name:

            if first_name.index(item1) != last_name.index(item2):
                print(f"{item1} {item2}")

