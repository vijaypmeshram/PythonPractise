# take input n, min , max and then see n diveded by min untill max is reached
# Distribution of apples with user given minimum and maximum choice

n = int(input("how many apples you have? \n"))
min = int(input("how much minimum numbers of apples you want to distribute? \n"))
max = int(input("how much maxmum numbers of apples you want to distribute? \n"))

while min <= max:
    remain=n % min
    if remain == 0:
        print(f"{n} apple can be divided in {min} parts ")
    else:
        print(f"{n} apple can not be divided in {min} parts ")
    min += 1
