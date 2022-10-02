
print("this is a function")

def func1(a , b):
    add=a+b
    print(add)
    return add

var1 = func1(110 , 10)

def func3(var1,a):
    sol = a/var1
    print(sol)

func3(var1, 250)


def func2():
    print("hello vjy")
    """this function output is none because it does not have return statement"""
    """if u remove print function it does not return none"""
print(func2())


print("lets say it 1")
nu1=input()
print("lets say it 2")
nu2=int(input())

try:
    num=nu1+nu2
    print(num)

except Exception as e:
    print(e)
print("check the values")