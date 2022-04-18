﻿import viz, vizfx, os
import vizmat, vizact
import numpy as np
from playsound import playsound
#from paint5Support import *
viz.setMultiSample(4)
viz.fov(60)
viz.go()
piazza = vizfx.addChild(r'C:\Users\hp\OneDrive\Desktop\VizardTutorial\paintingTP\Painting\cottage1.osgb')
#piazza1 = vizfx.addChild(r'C:\Users\hp\OneDrive\Desktop\VizardTutorial\paintingTP\Painting\blackboard.osgb')
piazza1 = vizfx.addChild(r'C:\Users\hp\OneDrive\Desktop\VizardTutorial\paintingTP\Painting\blackboard.osgb', pos=(-5,5.3,-9.2), euler = (180,0,0)) # pos=(6.3,5.3,0))
tempFlag = 0

drawList = []

def getDistance(listOfPoints):
    length = 0 
    for i in range(1,len(listOfPoints)):
        length += np.linalg.norm(listOfPoints[i], listOfPoints[i-1])
    return length

def circleClearCheck(pointList,r,threshold, centre, originalPerimeter):
	for point in pointList:
			dist = np.linalg.norm(point-centre)
			if dist<r-threshold and dist>r+threshold:
					return False
	perimeter = getDistance(pointList)
	if perimeter<originalPerimeter+threshold and perimeter>originalPerimeter-threshold:
		return True
	else:
		return False
			
def lineClearCheck(listOfPoints, threshold, originalLength=2):
    for point in listOfPoints:
        if point[0] < (-1) and point[0] > (-4) and point[1] < 3.5 and point[1] > 2.5:
            pass
        else:
            return False
    perimeter = getDistance(listOfPoints)
    if perimeter<originalLength+threshold and perimeter>originalLength-threshold:
        return True
    else:
        return False

def squareClearCheck(pointList,threshold,checkPointList, originalPerimeter):
	# checkPointList : left,right,top,bottom
	left,right,top,bottom = checkPointList
	for i in range(len(pointList)):
			perp1 = abs(left-pointList[i][1])
			perp2 = abs(right-pointList[i][1])
			perp3 = abs(top-pointList[i][0])
			perp4 = abs(bottom-pointList[i][0])
			allPerp = [perp1,perp2,perp3,perp4]
			index = allPerp.index(min(allPerp))
			if index==0:
					if perp1>threshold:
							return False
			elif index==1:
					if perp2>threshold:
							return False
			elif index==2:
					if perp3>threshold:
							return False
			elif index==3:
					if perp4>threshold:
							return False
	perimeter = getDistance(pointList)
	if perimeter<originalPerimeter+threshold and perimeter>originalPerimeter-threshold:
		return True
	else:
		return False

def addArrow(begin,end):
	ARROW_SIZE = 0.015
	#Find distance between points
	d = vizmat.Distance(begin,end)
	if tempFlag == 1:
		begin[2] = -9.1 
		end[2] = -9.1
	#Draw arrow line
	viz.startlayer(viz.LINES)
	viz.linewidth(8)
	viz.vertex(begin)
	viz.vertex(end)
	arrow = viz.endlayer()
	return arrow

polhemus = viz.add('polhemus.dle')
fastrak1 = polhemus.addFastrak()
print(polhemus.HEMI_POS_X)
fastrak1.setHemisphere(polhemus.HEMI_NEG_X)

def getPos():
	print(fastrak1.getPosition())
	return fastrak1.getPosition()

#file = open(r"C:\Users\devvrat joshi\downloads\data1.txt","r")
l = getPos()
arrow1 = addArrow(l,l)
arrow1.color(viz.GREEN)
prevR = l
r = l
#prevTime = os.path.getmtime(r"C:\Users\devvrat joshi\downloads\dataOneLine.txt")
def update():
	global l,r,prevR,prevTime
	#newTime = os.path.getmtime(r"C:\Users\devvrat joshi\downloads\dataOneLine.txt")
	#if newTime>prevTime:
	l = getPos()
	r = l
	r[0] = r[0]*10 
	r[1] = -r[1]*10
	r[2] = r[2]*10
	print(r)
	arrow1 = addArrow(prevR,r)
	arrow1.color(viz.GREEN)
	drawList.append(arrow1)
	prevR = r
	print("YES")
	#prevTime = newTime
vizact.ontimer2(0.2,10000,update)

level = 0

def level3():
	global level
	global drawList
	level = 3
	viz.startLayer(viz.POINTS)
	viz.pointSize(20)
	viz.vertexColor(1,0,0)
	viz.vertex(-1.5,3.0,-9.1)
	viz.vertex(-1.5603073543762191,3.342020075084167,-9.1)
	viz.vertex(-1.7339554635211587,3.6427874984245703,-9.1)
	viz.vertex(-1.9999998113248902,3.866025294852786,-9.1)
	viz.vertex(-2.3263515362618343,3.984807702570088,-9.1)
	viz.vertex(-2.673647820077866,3.984807816064741,-9.1)
	viz.vertex(-2.9999996226497094,3.866025621647621,-9.1)
	viz.vertex(-3.2660441163593292,3.6427879991033234,-9.1)
	viz.vertex(-3.43969242208275,3.342020689257616,-9.1)
	viz.vertex(-3.4999999999997864,3.000000653589793,-9.1)
	viz.vertex(-3.43969286916441,2.6579805390894276,-9.1)
	viz.vertex(-3.2660449565980256,2.357213002254457,-9.1)
	viz.vertex(-3.0000007547002965,2.133975031942419,-9.1)
	viz.vertex(-2.6736491073983903,2.0151924109249855,-9.1)
	viz.vertex(-2.3263528235825084,2.015192070441026,-9.1)
	viz.vertex(-2.0000009433759036,2.1339740515579146,-9.1)
	viz.vertex(-1.7339563037605097,2.357211500218198,-9.1)
	viz.vertex(-1.560307801458682,2.6579786965690815,-9.1)
	arrow = viz.endLayer()
	drawList.append(arrow)
vizact.onkeydown( '3', level3)

def level2():
	global drawList, level
	level = 2
	viz.startLayer(viz.POINTS)
	viz.pointSize(20)
	viz.vertexColor(1,0,0)
	viz.vertex(-3.5,2.0,-9.1)
	viz.vertex(-1.5,2.0,-9.1)
	viz.vertex(-3.5,4.0,-9.1)
	viz.vertex(-1.5,4.0,-9.1)
	arrow = viz.endLayer()
	drawList.append(arrow)
vizact.onkeydown( '2', level2)

def level1():
	global drawList,level
	level = 1
	viz.startLayer(viz.POINTS)
	viz.pointSize(20)
	viz.vertexColor(1,0,0)
	viz.vertex(-3.5,2.0,-9.1)
	viz.vertex(-1.5,2.0,-9.1)
	arrow = viz.endLayer()
	drawList.append(arrow)
vizact.onkeydown( '1', level1)
	

def clearDrawing():
	while drawList != []:
		drawList.pop().remove()

vizact.onkeydown('c', clearDrawing)

tempFlag = 0
def ontempFlagKeydown():
	global tempFlag
	if tempFlag==0:
		tempFlag = 1
	elif tempFlag==1:
		tempFlag = 0

# 1. Physical Space to Virtual Space
# 2. Workspace
# 3. Automatic
# 4. Audio -- completed
# 5. Boundary exit entry
# 6. Boundary start recording
# 7. Metric + Scoring
# 8. Time

path = ""

def playAudio():
	global path
	playsound(path)
	
circlePoints = [
	(-1.5,3.0,-9.1),
	(-1.5603073543762191,3.342020075084167,-9.1),
	(-1.7339554635211587,3.6427874984245703,-9.1),
	(-1.9999998113248902,3.866025294852786,-9.1),
	(-2.3263515362618343,3.984807702570088,-9.1),
	(-2.673647820077866,3.984807816064741,-9.1),
	(-2.9999996226497094,3.866025621647621,-9.1),
	(-3.2660441163593292,3.6427879991033234,-9.1),
	(-3.43969242208275,3.342020689257616,-9.1),
	(-3.4999999999997864,3.000000653589793,-9.1),
	(-3.43969286916441,2.6579805390894276,-9.1),
	(-3.2660449565980256,2.357213002254457,-9.1),
	(-3.0000007547002965,2.133975031942419,-9.1),
	(-2.6736491073983903,2.0151924109249855,-9.1),
	(-2.3263528235825084,2.015192070441026,-9.1),
	(-2.0000009433759036,2.1339740515579146,-9.1),
	(-1.7339563037605097,2.357211500218198,-9.1),
	(-1.560307801458682,2.6579786965690815,-9.1)
]

squarePoints = [
	(-3.5,2.0,-9.1),
	(-1.5,2.0,-9.1),
	(-3.5,4.0,-9.1),
	(-1.5,4.0,-9.1)
]

linePoints = [
	(-3.5,2.0,-9.1),
	(-1.5,2.0,-9.1)
]

def sound():
	global level
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

vizact.ontimer2(0.2,10000,sound)


chances = 10

def executeLevel1():
	clearDrawing()
	level1()
	return lineClearCheck()
	
def executeLevel2():
	clearDrawing()
	level2()
	return squareClearCheck(squarePoints, 0.5, , )

def executeLevel3():
	clearDrawing()
	level3()
	return circleClearCheck(circlePoints, 1, 0.5, (-2.5,3,9.1), 2*3.141592)

def main():
	for i in range(chances):
		cleared = executeLevel1()
		if cleared==True:
			break
		chances += 1
	if i==chances:
		exit()
	for i in range(chances):
		cleared = executeLevel2()
		if cleared==True:
			break
		chances += 1
	if i==chances:
		exit()
	for i in range(chances):
		cleared = executeLevel3()
		if cleared==True:
			break
		chances += 1
	if i==chances:
		exit()




vizact.onkeydown( 'a', ontempFlagKeydown)