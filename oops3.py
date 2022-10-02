class Teacher:
    def __init__(self, name , subject):
        super().__init__()
        self.name = name
        self.subject = subject

    def A(self):
        return print(f"hello, I am your teacher {self.name}. I will teach you {self.subject}")

class Swipper:
    def __init__(self, name , work):
        self.name = name
        self.work = work

    # def B(self):
    #     return print(f"hello, My name is {self.name}. I do {self.work}")



class Employee(Teacher, Swipper):
    leaves = 20

    @classmethod
    def allowed_leaves(cls, alleaves):
        cls.leaves = alleaves



class management(Employee):
    pass




mohan = Employee("mohan", "math")
# sharma = management()

# sharma.name = "rahul"

mohan.name = "mohan"
mohan.post = "manager"
mohan.salary = 2200
mohan.pcname = "Dell"
mohan.leaves = 22

meshram = management("Meshram", "history")
bansod = Employee("Bansod", "biology")

raut = Employee("Pramod", "swipper")
# dok = Employee()

# print(bansod.A())
# print(meshram.A())
print(raut.B())
# print(sharma.name)