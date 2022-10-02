

# ls = os.listdir()
#
# for i in ls:
#     str = i
#     upp = str[0].upper() + str[1:]
#     # print(upp)
#
# x = 1
# # src = os.getcwd()
#
# src = os.listdir(input("type your directory"))
# for i in src:
#     # print("im here")
#     if i.endswith(".txt"):
#         print("imhere")
#         os.rename(i, str(x)+".txt")
#         x = x + 1
#         print("program executed")
#         break

import os
# first u have take folderpath from user
src = str(input("Enter your folder path here \n"))

# second u have to ask use rto change first letter of files in that folder
# ask = str(input("Do you want to change first letter of files to uppercase in this folder? \n"))
# ls = os.listdir(src)
# if ask == "yes":
#     for i in ls:
#         change1letter = i
#         upp = change1letter[0].upper() + change1letter[1:]
        # print(upp)

# third you ask user to change extension of jpg file name to numbers
changename = str(input("Do you want to change the name of files with extension of .jpg to numbers? \n"))
if changename == "yes":
    ls = os.listdir(src)
    num = 1
    for file in ls:
        try:
            if file.endswith(".JPG"):
                getfile = file
                chg = f"photo_{num}.jpg"
                original_name = os.path.join(src, getfile)
                new_name = os.path.join(src, chg)
                filenamechange = os.rename(original_name, new_name)
                num+=1
                print(filenamechange)

        except Exception as e:
            print(e)
            print("name already exist")


