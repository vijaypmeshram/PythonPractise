
mylist=[]
size = int(input("Enter the size of list \n"))
for i in range(size):
    mylist.append(input("Enter the list element \n"))

print(mylist)
rev = mylist[:]
rev.reverse()
print(f"your list {mylist} is reversed as {rev}")

print(f"your list {mylist} is reversed as {mylist[::-1]}")

mylis = mylist[:]
for i in range(len(mylis)//2):
    mylis[i], mylis[len(mylis) -i -1] = mylis[len(mylis) -i -1], mylis[i]

print(f"the original {mylist} is reverved as {mylis}")