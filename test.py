# dict = {'pay':'200', 'con':'manu', 'gst':44}
#
# dict.update({'pay':'kk'})
# print(dict)

# def touch(num, str):
#     t= num*str
#     print(t)
#
# touch(4,'run')

# while True:
#     print('Run ')

# import time
#
# while time.sleep(10):
#     def exercise():
#         exercise()
#         print('hands straight')
#         time.sleep(3)
#         print("hands up")
#         time.sleep(3)
#         print("hands beside")
#         time.sleep(3)
#         print('hands down')

# creating string list of sentences
# take input from user and input convert in to lower case
# match the most relevant search and give output in descending order
import re
def macth(sen1, sen2):
    words1 = sen1.split(" ")
    words2 = sen2.split(" ")
    score = 0
    for item in words1:
        for item in words2:
            if item.lower() == item.lower():
                score +=1
    return score

ls= ['this is python program', 'here, python is not python snake',
     'python used to write program and widely used for its multi functionality']
# lt = 'python used to write program and widely used for its multi functionality'
# user_q = input("Enter your search keyword: \n")
# uslower= user_q.lower()
#
# for i in range(len(ls)):
#     x = re.search(uslower, ls[i])
#     if uslower in ls[i]:
    #     scores = [macth(uslower, item) for item in ls]
    #     sortScores = [sortScore for sortScore in sorted(zip(scores, ls), reverse=True)]
        # print(sortScores)
        # for score, item in sortScores:
        #     print(item)
        # print(ls[i])
        # print("Not found")
    # else:
    #     print(f' search found in {ls[i]}')


data = {"mylist": [{
    'name': "car",
    'getValue': True,
    'list2': [11, 12, 13, 14, 15, 16, 17, 18, 19]
     },

    {
        'name': "movie",
        'getValue': True,
        'list2': [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
    }
]
}

# jsonls = json.dumps(data)
# print(jsonls)
userin = int(input("ENter the number : \n"))
# print(type(userin))
dictvalue = data["mylist"]
# print(type(dictvalue))

for lists in dictvalue:
    items = lists['list2']
    # print(type(items))
    for i in items[:]:
        if userin == i:
            print(lists)
            getname = lists['name']
            print(getname)
            # print(dictvalue.)

