import time

def searcher():
    print("reading some text")
    book = "hi this is vijay i am learning python computer language i am glad that i have rich knowledge of computer programing"
    time.sleep(4)

    while True:
        text = (yield )
        if text in book:
            print("your text found in book")
        else:
            print("your text does not found in book")

search = searcher()
next(search)
search.send("hi")
search.send("have")
search.send("below")



