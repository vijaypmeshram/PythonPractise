class student:
    my_class_name = "chemistry"

    def __init__(self, vay, adnav, sit):
        self.seat_no = sit
        self.age = vay
        self.surname = adnav


rohit = student(11, "sah", 22)


my_class_name = "physics"
print(student.my_class_name)
print(rohit.my_class_name)
rohit.my_class_name = "bio"
print(rohit.my_class_name)
print(student.my_class_name)
#
#
#
#     # def printdeatails(self):
#     #     return (f"hi, my surname is {self.surname}. I am {self.age} years old. imy seat number is {self.seat_no}")
#
#
# rohit = student()
#
# rohit.age = 22
# rohit.surname = "sakhare"
# rohit.seat_no = 2
# #
# # print(rohit.printdeatails())
# print(rohit.age)
# # print(subodh.printdeatails())
# # print(subodh.age)