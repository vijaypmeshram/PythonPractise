# need function which take input through microphone and then print in file
import pyaudio
import SpeechRecognition as sr


def mainfuction(source):
    r = sr.Recognizer(source)
    audio = r.listeb(source)
    user = r.recognize(audio)
    user = ""

    try:
        print(user)
    except Exception as e:
        print(e)

def record(source):
    # open microphone and record4
    pass

# def nwrite()
#     with open("recording.txt", "a") as f:
#         f.write(msg)

if __name__ == '__main__':
    with sr.Microphone() as source:
        while True:
            mainfuction(source)

    record()