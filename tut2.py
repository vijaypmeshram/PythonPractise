temp=["two","tomato","fuel"]

#temp.remove("two")
#temp.append(2)
#temp.insert(2,"me")

#print(temp)
a="three is my fav number"
b="7"
#print(a.startswith("t"))

a1={"A":"apple", "B":"ball", "C":"cat"}
a1["D"]="dog"
#print("Enter your alphabet to get meaning of it")
#In=input()
#a1.update({"E":"elephant"})
#print(a1.items())
#print(a1[In])

#s = set([1, 2, 3, 4, 5])
#s.add(6)
#s1= s.intersection({1, 3, 7, 9, 4})

#print(s.isdisjoint(s1))

# print("Enter your age")
# var1 = int(input())
#
# if var1>100:
#     print("please check your age")
# elif var1<8:
#     print("please check your age")
# elif var1>18:
#     print("you r eligible for driving")
#
# elif var1==18:
#     print("lets check your drive in person")
# else:
#     print("you r not eligible for driving")


print("enter your operator")
op = input()
print("enter your first number")
num1 = int(input())
print("enter your second number")
num2 = int(input())

if op=="*":
    if num1==45 and num2==6:
        print(555)
    else:
        num4=num1*num2
        print(num4)
elif op=="+":
    if num1==56 and num2==4:
        print(77)
    else:
        num4=num1+num2
        print(num4)
elif op=="/":
    if num1==56 and num2==4:
        print(4)
    else:
        num4=num1/num2
        print(num4)