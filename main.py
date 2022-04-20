from datetime import datetime
import imp
import viz, vizfx, os, time
import vizmat, vizact
import numpy as np
import vizinput
import winsound
from datetime import datetime
from winsound import PlaySound
from allPoints import *
from metric import *
# from levelsHello import *
# from playSound import * 
from paint import *

viz.setMultiSample(4)
viz.fov(60)
viz.go()
viz.MainView.move([-3,0,-3])
viz.MainView.setEuler([180,0,0])
piazza = vizfx.addChild(r'C:\Users\hp\OneDrive\Desktop\VizardTutorial\paintingTP\Painting\cottage1.osgb')
piazza1 = vizfx.addChild(r'C:\Users\hp\OneDrive\Desktop\VizardTutorial\paintingTP\Painting\blackboard.osgb', pos=(-5,5.3,-9.2), euler = (180,0,0)) # pos=(6.3,5.3,0))

vizact.onkeydown('c', clearDrawing)

#vizact.onkeydown('a', ontempFlagKeydown) #todo always project on the screen 


vizact.ontimer2(0.2,10000,update)
userName = vizinput.input('Enter your name:')
flag = 0
wait = 0
chances = 0
allowedChances = 10
startPoint = 0
endPoint = 0
level = 0
levelOn = 0
timeOut = 30
changeit = 0
originalPerimeterCircle = 6.28
originalPerimeterSquare = 8
centre = np.array([-2.5,3,-9.1])
checkPointList = [-1.5,-3.5,4,2]
threshold = 0.5

fileName = userName + '.txt'
myFile = open(fileName, "w+")
myFile.write('User Name: '+ userName + '\n')
def reachedPointStartLevel():
    point = np.array(getPos())[:2]
    point[0] *= 10 
    point[1] *= -10
    global flag, wait, collectionList, timer, text_2D_screen, changeit, threshold, centre, checkPointList, levelOn, level, chances, timecollectionList
    if levelOn==1:
        if timer>timeOut:
            changeit = 0
            flag = 0
            levelOn = 0
            flag = 0
            levelOn = 0
            if level==1:
                levelDone,score = lineClearCheck(collectionList, threshold, originalLength=2)
            if level==2:
                levelDone,score = squareClearCheck(collectionList, threshold, checkPointList, originalPerimeterSquare)
            if level==3:
                levelDone,score = circleClearCheck(collectionList, r, threshold, centre, originalPerimeterCircle)
            if levelDone==True:
                myFile.write('Level'+str(level)+ ': ' + str(collectionList) + '\n' 
                             + 'TimeStamp: ' + str(timecollectionList) + '\n'
                            + 'levelDone: ' + str(levelDone) + ' Score: ' + str(score) + '\n')
                if level==3:
                    myFile.write('You WON' + '\n')
                    myFile.close()
                    vizinput.message('You WON!!!')
                else:
                    vizinput.message('Yipeee..Level {} Cleared, Score: '.format(level,score))
            if levelDone==False:
                myFile.write('Level'+str(level)+ ': ' + str(collectionList) + '\n'
                             + 'TimeStamp: ' + str(timecollectionList) + '\n' 
                            + 'levelDone: ' + str(levelDone) + ' Chances left: ' + str(allowedChances-chances) + '\n')
                chances += 1
                level -= 1
                if chances<allowedChances:
                    vizinput.message('Oops..Try Again. {} Chance remaining'.format(allowedChances-chances))
                else:
                    myFile.close()
                    vizinput.message('You LOST!!!')
            text_2D_screen.remove()
            changeLevel()
            
    if level>0:
        print('Hello1')
        print(point, startPoint,np.linalg.norm(point-startPoint))
        print('Hello2')
        if np.linalg.norm(point-startPoint)<0.10 and flag==0 and levelOn==0:
            flag = 1
            collectionList = []
            timecollectionList = [] 
            timer = 0
            text_2D_screen = viz.addText(str(timer),parent=viz.SCREEN)
            timer += 1
            changeit = 1
            levelOn = 1
            clearDrawing()
            if level==1:
                level1()
            if level==2:
                level2()
            if level==3:
                level3()
        elif np.linalg.norm(point-endPoint)<0.10 and flag==1 and levelOn==1:
            changeit = 0
            flag = 0
            levelOn = 0
            if level==1:
                levelDone,score = lineClearCheck(collectionList, threshold, originalLength=2)
            elif level==2:
                levelDone,score = squareClearCheck(collectionList, threshold, checkPointList, originalPerimeterSquare)
            elif level==3:
                levelDone,score = circleClearCheck(collectionList, threshold, centre, originalPerimeterCircle, r=1)
            print('LevelDone', levelDone)
            if levelDone==True:
                myFile.write('Level'+str(level)+ ': ' + str(collectionList) + '\n' 
                             + 'TimeStamp: ' + str(timecollectionList) + '\n'
                            + 'levelDone: ' + str(levelDone) + ' Score: ' + str(score) + '\n')
                if level==3:
                    vizinput.message('Yipeee..Level {} Cleared, Score: {}'.format(level,score))
                    myFile.write('You WON' + '\n')
                    myFile.close()
                    vizinput.message('You WON!!!')
                else:
                    vizinput.message('Yipeee..Level {} Cleared, Score: {}'.format(level,score))
            if levelDone==False:
                myFile.write('Level'+str(level)+ ': ' + str(collectionList) + '\n' 
                             + 'TimeStamp: ' + str(timecollectionList) + '\n'
                            + 'levelDone: ' + str(levelDone) + ' Chances left: ' + str(allowedChances-chances) + '\n')
                chances += 1
                level -= 1
                if chances<=allowedChances:
                    vizinput.message('Oops..Try Again. {} Chance remaining'.format(allowedChances-chances))
                else:
                     myFile.close()
                     vizinput.message('You LOST!!!')
            text_2D_screen.remove()
            changeLevel()
            # text_2D_screen.remove()
            # timer stop
    
        
vizact.ontimer2(0.2,10000,reachedPointStartLevel)

timer = 0
text_2D_screen = viz.addText(str(timer),parent=viz.SCREEN)
text_2D_screen.remove()

def changeLevel():
    global level, startPoint, endPoint
    if level==0:
        startPoint = np.array([-1.5,2.0]) 
        endPoint = np.array([-3.5,2.0])
        level = 1
        clearDrawing()
        level1()
    elif level==1:
        startPoint = np.array([-1.5,2.0])
        endPoint = np.array([-1.75,2.0])
        level = 2
        clearDrawing()
        level2()
    elif level==2:
        level = 3
        startPoint = np.array([-1.5,3.0])
        endPoint = np.array([-1.5,2.75]) ##
        clearDrawing()
        level3()
    elif level==3:
        clearDrawing()
        print('I WON')
        #youWon()
        
changeLevel()


def ontimerChange():
    global changeit, flag
    if changeit==1:
        global timer
        global text_2D_screen
        text_2D_screen.remove()
        text_2D_screen = viz.addText(str(timer),parent=viz.SCREEN)
        timer += 1
    

vizact.ontimer2(1,10000,ontimerChange)

def collectPoints():
    global flag, collectionList, timecollectionList
    if flag==1:
        r = getPos()
        r[0] = r[0]*10 
        r[1] = -r[1]*10
        r[2] = -9.1
        collectionList.append(r)
        timecollectionList.append(datetime.now())

vizact.ontimer2(0.2,10000,collectPoints)
path = './dingSound.mp3'

def playAudio():
    global path
    sound = viz.addAudio(path) 
    sound.volume(.5) 
    sound.play() 

def sound1():
    global level,levelOn, linePoints, squarePoints, circlePoints 
    if levelOn==1:
        r = getPos()
        r[0] = r[0]*10 
        r[1] = -r[1]*10
        r[2] = -9.1
        if level==1:
            points = linePoints
        elif level==2:
            points = squarePoints
        elif level==3:
            points = circlePoints
        for i in points:
            if np.linalg.norm(np.array(i)-np.array(r))<0.3:
                playAudio()
                break
vizact.ontimer2(0.2,10000,sound1)