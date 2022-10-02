class Employee:
    leaves = 20

    @classmethod
    def allowed_leaves(cls, alleaves):
        cls.leaves = alleaves



mohan = Employee()
sharma = Employee()

mohan.post = "manager"
mohan.salary = 2200
mohan.pcname = "Dell"
mohan.leaves = 22
# print(Employee.leaves)
mohan.allowed_leaves(23)

# print(mohan.leaves)
# print(Employee.leaves)
# print(Employee.leaves)


# static methhod

class Student:

    def __init__(self, first, second, third):
        self.name = first
        self.middle = second
        self.surname = third

    @classmethod
    def change_name(cls, string):
        params = string.split("-")
        # print(params)
        """
        It is necessary to mention all three parans idexes in return statement
        as you have to call three values(mention) from init function
        """
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

# shiv = Student("raks", "shambu", "dhar")
raju = Student.change_name("pramod-shantila-raut")

# print(shiv.sname)
print(raju.surname)

