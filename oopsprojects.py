class Electronics_device:

    def __init__(self, model, price, color, screen):

        self.model = model
        self.price = price
        self.color = color
        self.screen = screen

    item = "mobile"
    instock = 200
    company = "whirlpool"

    def iscompany(self):
        return print(f"the company name is {self.company}")

class pocket_gadget(Electronics_device):
    def __init__(self):
        super().__init__()
        self.model = "my phone"

    device_name = "Iwatch"
    item = "watch"


class phone(pocket_gadget):

    # company = "Nokia"

    def myphone(self):
        return print(f"my fone is {self.model}")


nokia1110 = phone("Nokia 1110", 6000, "blue", "small screen")
vivo12  = pocket_gadget("Vivo 12", 21000, "white", "big screen")
realmeXT = Electronics_device("Realme XT", 18000, "Black", "Big Screen")
# iphone = pocket_gadget()

# print(vivo12.myphone())
# print(nokia1110.iscompany())
# print(nokia1110.model)
# print(realmeXT.price)

class A:
    var1 = "this is var1 in A"
    def __init__(self):
        self.var2 = "this instance is var2 in A"
        self.var1 = "this instance is var1 in A"

class B(A):
    var1 = "this is var1 in B"
    def __init__(self):
        super().__init__()
        self.var2 = "this is var2 in B"

a = A()
b = B()

print(b.var1)