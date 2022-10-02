from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        return print("the area is")



class circle(shape):
    def __init__(self, radius, pie):
        self.radius = radius
        self.pie = pie
        # self.mail = f"{radius}.{pie}@vk.com"

    # def circle1(self):
    #     return self.radius * self.pie

    def area(self):
        # return self.radius * self.pie
        pass
    @property
    def email(self):
        return f"{self.radius}.{self.pie}@vk.com"

    @email.setter
    def email(self, string):
        print("new setting now...")
        c = string.split("@")[0]
        self.radius = c.split(".")[0]
        self.pie = c.split(".")[1]


raju = circle("R", "P")

print(raju.email)

# raju.radius = "diameter"
# print(raju.email)
# raju.email = "1.2@pk.com"
# print(raju.pie)


# cr = circle()
# print(cr.circle1())
# print(cr.area())


def red(n):
    for i in range(n):
        # print(i)
        yield i
        """yield function is generator. which generate value one by one"""
b = red(5)

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
