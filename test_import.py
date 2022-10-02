# import enum_join
# it is mecesary to add file name to use function from that file

# l = enum_join.list
# a = " and ".join(l)
# print(a)

# set1 = set([1, 2, 3, 4, 5, 6, 7])
# print(type(set1))
# def sq(x):
#     x=x*x
#     return x
# ls = list(map(lambda x:x*x, set1))
# print(ls)

# def is_GT6(x):
#     return x>2
# ls = list(filter(is_GT6, set1))
# print(ls)

# from functools import reduce
#
# # list1=[1,2,3,5,67,98,6]
# ls= reduce(lambda x,y:x+y, set1)
# print(ls)


x = int(input())
while x>=0:
    var = "x"
    for i in range(x,0,-1):
        print(var*x)
        x -= 1
    break