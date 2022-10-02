#   "HEALTH MANAGEMENT SYSTEM"

print("What fo you want")
print(" 1.Entry or 2. Retrive")

selection_1 = int(input())

if selection_1 == 1:
    print("select your name")
    print("1.Rahul, 2.Monty, 3.Neha")

    selection_2 = int(input())

    if selection_2 == 1 :
        rahul = open("rahul.txt", "a")
        print("write now")

        def dataEn():
            var = input()
            import datetime
            return var, datetime.datetime.now()
        dataEn()
        rahulEn = dataEn()
        rahul.write(str(rahulEn))
        rahul.close()
        print("Rahul, your entry is submitted successfully")

    if selection_2 == 2:
        monty = open("monty.txt", "a")
        print("write now")
        def dataEn():
            var = input()
            import datetime
            return var, datetime.datetime.now()
        dataEn()

        montyEn = var
        monty.write(str(montyEn))
        monty.close()
        print("Monty, your entry is submitted successfully")

    if selection_2 == 3:
        neha = open("neha.txt", "a")
        print("write now")
        def dataEn():
            var = input()
            import datetime
            return var, datetime.datetime.now()
        dataEn()

        nehaEn = dataEn()
        neha.write(str(nehaEn))
        neha.close()
        print("Neha, your entry is submitted successfully")

if selection_1 == 2:
    print("select your name")
    print("1.Rahul, 2.Monty, 3.Neha")

    selection_2 = int(input())

    if selection_2 == 1 :
        rahul = open("rahul.txt")
        print(rahul.read())
        rahul.close()

    if selection_2 == 2:
        monty = open("monty.txt")
        print(monty.read())
        monty.close()

    if selection_2 == 3:
        neha = open("neha.txt")
        print(neha.read())
        neha.close()