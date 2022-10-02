lis = ["H", "A", "B", "C"]
norm = 44
kwvjy = {"A":"Apple", "B":"Bat", "C":"Cat"}
def fun1(norm, *args, **kwargsvjy):
    print(norm)
    # print(args)
    # for i in args:
    #     print(i)
    for key,value in kwargsvjy.items():
        # print(key,value)
        print(f"this {key} belongs to {value}")
fun1(norm, *lis, **kwvjy)

# import time
#
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# l=0
# for i in range(10):
#     print("its happening")
# init=time.time()
# print(init)

# k=0
# while (k<1):
#     print("remaining time is")
#     time.sleep(2)
#     k+=1

from filehandling import a
print(a)