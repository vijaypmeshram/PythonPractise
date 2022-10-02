# you have created schedule for a person
#     drink water after every 45min
#     clean his eyes after every 20min
#     wash his hands after evry 30min
# and created log for person

from datetime import datetime
from pygame import mixer
# need to install pygame

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def logmsg(msg):
    with open("logsheet.txt" "a") as f:
        f.write(f"{msg}, {datetime.now()}")

if __name__== "__main__":
    init_water = time()
    init_eyes = time()
    init_exer = time()
    water_time = 5
    eyes_time = 3
    hands_time = 4
    while True:
        if time() - init_water > water_time:
            print("now you have to drink water. type stop to stop the music")
            musicloop("water.mp3", "stop")
            init_water = time()
            logmsg("water is drank at ")
