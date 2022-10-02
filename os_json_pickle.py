import os

# print(os.getcwd())
# print(dir(os))
os.chdir("c://")
# print(os.getcwd())
# print(os.listdir())
# os.makedirs("this/that")

# os.rename("vjy.txt", "raj.txt")


import json

cars = {"4wheel":"sumo",
        "2wheel":"pulser",
        "ls1":[1,2,3,5],
        "isport": False}
# parsed = json.loads(cars)
# print(parsed["2wheel"])

comp = json.dumps(cars, sort_keys=True)
# print(comp)


import pickle

dish = ["bhendi", "karela", "rayta"]
file = "mydish.pkl"
fileobj = open(file, "wb")
pickle.dump(dish, fileobj)
# print(fileobj)
fileobj.close()
