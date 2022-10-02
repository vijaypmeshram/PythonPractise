import time
from functools import lru_cache

@lru_cache(maxsize=20)
def getnum(n, num1, num2):
    sum = num1 + num2
    # print("do some work")
    time.sleep(n)
    # print("next work")
    return n, sum

if __name__ == '__main__':
    print("load first page")
    getnum(3, 5, 7)
    print("load second page")
    getnum(3, 4, 4)
    print("loading first page again")


