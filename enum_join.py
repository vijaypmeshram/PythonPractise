list = ["shyam", "ram", "bharat","kunti", "bhim", "dic", {"p1":"voice", "p2":"vijay", "va":[3, "k"]}]
# print(list)

# for index, item in enumerate(list):
#     if index%2==0:
#         print(item)
# a = " and ".join(list)
# print(a)

# list.reverse()
# list.index()
# list.insert(5,"gabru") it get two argument, first is index and another item
# list.sort()   '<' not supported between instances of 'dict' and 'str'
# list.pop(1)   pop func take index value in list
# list.remove("dic") remove func take item to remoove from list
# ls_copy = list.copy()
# list.append("bol") append func add item at end of the list


# # for numveric list
# squar = []
# for x in range(1,11):
#     squar.append(x**2)
# print(squar)

# first_2list = list[:2]           slicing of list from index 1 to 2, it does not take o index item
# listslice =list[3:5]         slice list take item in 4 no index to 5 no index

# print(listslice)

# tp = (12, "binod")
# print(type(tp))          in tuple , items cannot be modified

# if "shyam" not in list:       to find item in list and take appropriate action
#     print("beautifull")
# else:
#     print("not good")


# isgame_active = [3]
# if isgame_active:
#     print("true")       to reutn value true, varible should be filled with item. otherwise it return false
# else:
#     print("false")
# "l1":"rohit", "l2":"bablu", "point":77,
# Dictionary
Dict = {"l4":{"g1":43, "h1":22, "f1":44, "g1":655}, "l5":{"k1":64, "h1":87}}
# AssDict= Dict['l4']    to get value of that key
# print(Dict.keys())           retrun the keys of dict .. does not return the key of keys in dic
# Dict["hell"] = "no"             this add key and value onto the dict

# del Dict["l1"]            this delete the key value pair from dict by using delete function
# looping through all keys
# for name in Dict.keys():
    # print(name)            return all keys(class_str) in Dict
# print(Dict)

# looping thrigh all values
# for value in Dict.values():
#     print(value)            return all the value of that keys in Dicy

# getting values of of common keyword
# dict = Dict['l4']
# print(dict['h1'])
# for get in Dict:
#     print(get['h1'])


#while loop with empty string
# msg = ''
# while msg != 'quit':
#  msg = input("What's your message? ")
#  print(msg)
#  break

 # Store people's favorite languages.
fav_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

 # Show each person's favorite language,
# in order by the person's name.
for name, language in sorted(fav_languages.keys()):
 print(name + ": " + language)
# for name, language in fav_languages.items():
#  print(name + ": " + language)