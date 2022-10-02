# this program is used to find your age on 2090 with respect to 2022 because it written of Jan 2022
# this is a simple program does not use any module but simple math.
# so if you want to run program with current year then write following code after deleting current_year variable

# import datetime
# get_date = datetime.date.today()
# current_year = get_date.year


if __name__ == '__main__':
    print("welcome to the programe. you will get your age on 2090.")
    print("this programm written in 2022 so you will get your age with respect to 2022")

    while True:
        print("please select following option that you want to find out your age on 2090")
        print("1. Age")
        print("2. Year of birth")
        print("3. if you want to exit the program")
        user_choice = input()
        current_year = 2022
        if user_choice == '1':
            try:
                current_age = int(input("Enter your current age in figure: \n"))
                diff_yr = 2090 - current_year
                useron2090 = diff_yr + current_age
                if useron2090 >= 100:
                    print(f"your age on 2090 is {useron2090} years")
                    print("Congrats, you completed a century.")
                else:
                    print(f"your age on 2090 is {useron2090} years")
            except Exception as e:
                print(e)
                print("it seems you entered invalid input. please entered the valid input")

        elif user_choice == '2':
            try:
                birth_yr = int(input("Enter your year of birth: \n"))
                current_age = current_year - birth_yr - 1
                diff_yr = 2090 - current_year
                useron2090 = diff_yr + current_age
                if useron2090 >= 100:
                    print(f"your age on 2090 is {useron2090} years")
                    print("Congrats, you completed a century.")
                else:
                    print(f"your age on 2090 is {useron2090} years")
            except Exception as e:
                print(e)
                print("it seems you entered invalid input. please entered the valid input")

        elif user_choice == '3':
            print("Thank you for using this program")
            exit()

        elif user_choice != ['1', '2']:
             print("please entered the valid input")
             continue
        else:
            break