# rohan write program for multiplication of a number
# but he done wrong in few table for his benefits
# you have to write program that check rohan table function
# then return none if table is correct otherwise make correction with index in that table
# tell student that rohan is fraud

# class table:
#     def rohantable(self, number):
#         itemlist = []
#         if number == 6:
#             num = 0
#             while num <= 9:
#                 num += 1
#                 if num == 7:
#                     mul = 43
#                     itemlist.append(mul)
#
#                 elif num == 3:
#                     mul = 19
#                     itemlist.append(mul)
#
#                 else:
#                     mul = number * num
#                     itemlist.append(mul)
#
#             return itemlist
#         else:
#             num = 0
#             while num <= 9:
#                 num += 1
#                 mul = number * num
#                 itemlist.append(mul)
#         return itemlist
#
#     def numtable(self, number):
#         num = 0
#         itemlist=[]
#         while num <= 10:
#             num+=1
#             mul = number * num
#             itemlist.append(mul)
#         return itemlist
#
#     def iscorrect(self, item_1, item_2):
#         item_1.sort()
#         item_2.sort()
#         if (item_1 == item_2):
#             print(f"not equal at {item_1}")
#         else:
#             print("equal")
#         def compare(item_1, item_2):
#             for val
#
#
#
#
# if __name__ == '__main__':
#     print("Welcome to multiplication table program")
#     number = int(input("Enter the number: \n"))
#     user = table()
#     print(user.rohantable(number))
#     item_1 = user.rohantable(number)
#     item_2 = user.numtable(number)
#     print(user.iscorrect(item_1, item_2))


import random

def babunmul(number):
    wrong = random.randint(0,9)
    table = [i *number for i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(0,9)
    return table

def findwrongind(number, table):
        for i in range(1,11):
            # below identify index of wrong number
            if table[i-1] != i * number:
                return i

if __name__ == '__main__':
    # print(rohanmul(6))
    number = int(input("Enter the number: \n"))
    myTable = babumul(number)
    print(myTable)
    wrongnum = findwrongind(number, myTable)
    print(f"the number is wring at {wrongnum}")

