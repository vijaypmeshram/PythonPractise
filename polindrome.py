# num = input("Enter the number \n")
#
# ls = list(num)
# print(ls)
def polindrome(n):
    n=n+1
    while not is_polindrome(n):
        n+=1
    return n
def is_polindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter the cases:\n"))
    number = []
    for i in range(n):
        num = int(input("Enter the number: \n"))
        number.append(num)
# Below line give the next polindrome of a numbers in a list
    for i in range(n):
        print(f" the polindrawn of {number[i]} is {polindrome(number[i])}")

# Below program written considering single digit number will not give next number as per above
# programm, so that before running following program its is important comment out above two line

    seg = []
    for items in number:
        if items >= 10 :
            seg.append(items)

        elif items < 10:
            print(f"polindrome cannot be determin as the number {number[item]} is single digit")
    ls = len(seg)

    for i in range(ls):
        print(f" the polindrawn of {seg[i]} is {polindrome(seg[i])}")
