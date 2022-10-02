# api = 81d81c2bcee04823a149a3f9e2c63291
import json, requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

def callme():
    speak("top 10 news of the day")
    api_key = "81d81c2bcee04823a149a3f9e2c63291"
    api = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    call = requests.get(api).text
    parsed = json.loads(call)
    dict = parsed['articles']
    for article in dict:
        print(article['title'])
        speak(article['title'])
        speak("moving to the next news..")
    speak("thats for today. thanks for listening")

if __name__ == '__main__':
    speak("hello, mister vijay")
    callme()




