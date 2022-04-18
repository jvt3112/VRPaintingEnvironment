from playsound import playsound
import numpy as np
from allPoints import *
from levelsHello import *

path = r"C:\Users\hp\Downloads\dingSound.mp3"

def playAudio():
    global path
    playsound(path)

def sound():
    global level,levelOn
    if levelOn==1:
        point = getPos()
        if level==1:
            points = linePoints
        elif level==2:
            points = squarePoints
        elif level==3:
            points = linePoints
        for i in points:
            if np.linalg.norm(np.array(i)-np.array(point))<0.3:
                playAudio(path)
                break
