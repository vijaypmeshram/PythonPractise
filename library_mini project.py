
class library():
    def __init__(self, list, name):
        self.list = list
        self.name = name
        self.lendDict = {}
        self.library = 'ProgrammingBooks'

    def lendbook(self, user, book):
        if book not in self.list:
            print("Book is not exist in library")
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("lender book is updated you can lend a book")
                self.list.remove(book)
            else:
                print(f" book is already lended out by {self.lendDict[book]}")


    def returnbook(self, book):
        if book not in self.lendDict.keys():
            self.list.append(book)
            print("book is return at library")


    def addbook(self, book, user):
        if book in self.list:
            print("book already exist in library")
        else:
            self.list.append(book)
            print(f"{user} added the {book} book in the library")


    def removebook(self, book):
        if book not in self.list:
            print("you cannot the book. because it does not exist in library")
        else:
            self.list.pop(book)
            print(f"{user} removed the {book} book from library")


if __name__ == '__main__':
    my_books = library(['python', 'c++', 'java', 'html', 'asp.Net'], 'raj')
    print(f"welcome to the {my_books.name} library")

    while True:

        print('What do you want to do. please select the index of your choice')
        print("1. Lend a book")
        print("2. return a book")
        print("3. add a book into the library")
        print("4. remove a book from library")
        print("5. exit from the library program")

        user_choice = input()

        if user_choice == '1':
            print("Enter your name: ")
            user = str(input())
            print("Enter the name of a book")
            book = input()
            my_books.lendbook(user, book)

        elif user_choice == '2':
            print("Enter your name: ")
            user = str(input())
            print("Enter the name of a book")
            book = input()
            my_books.returnbook(book)

        elif user_choice == '3':
            print("ENter your name: ")
            user = str(input())
            print("Enter the name of a book")
            book = input()
            my_books.addbook(book, user)


        elif user_choice == '4':
            print("ENter your name: ")
            user = str(input())
            print("Enter the name of a book")
            book = input()
            my_books.removebook(book)

        elif user_choice == '5':
            print(f"\n Thnak you for visiting {my_books.name} library. see you soon")
            exit()

        else:
            try:
                if user_choice != ['1', '2', '3', '4', '5']:
                    print("kindly check your input")
                    continue
                else:
                    break
            except Exception as e:
                print(e)

        print("Print q to exit the programe or enter c to continue")
        user_input = input()
        while True:
            if user_input == "q":
                exit()
            elif user_input == "c":
                break
            else:
                print("please check your input")




