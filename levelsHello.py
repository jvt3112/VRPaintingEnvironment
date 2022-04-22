import viz, vizact
from playsound import playsound
import numpy as np

drawList = []

# Polhemus
polhemus = viz.add('polhemus.dle')
fastrak1 = polhemus.addFastrak()
print(polhemus.HEMI_NEG_X)
fastrak1.setHemisphere(polhemus.HEMI_NEG_X)

def getPos():
    print(fastrak1.getPosition())
    return fastrak1.getPosition()

def level3():
    global level
    global drawList
    level = 3
    viz.startLayer(viz.POINTS)
    viz.pointSize(20)
    viz.vertexColor(0,1,0)
    viz.vertex(-1.5,3.0,-9.1)
    viz.vertexColor(1,0,0)
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
    viz.vertexColor(0,0,1)
    viz.vertex(-1.5,2.75,-9.1)
    arrow = viz.endLayer()
    drawList.append(arrow)

def level2():
    global drawList, level
    level = 2
    viz.startLayer(viz.POINTS)
    viz.pointSize(20)
    viz.vertexColor(0,1,0)
    viz.vertex(-1.5,2.0,-9.1)
    viz.vertexColor(1,0,0)
    viz.vertex(-3.5,2.0,-9.1)
    viz.vertex(-3.5,4.0,-9.1)
    viz.vertex(-1.5,4.0,-9.1)
    viz.vertexColor(0,0,1)
    viz.vertex(-1.65,2.0,-9.1)
    arrow = viz.endLayer()
    drawList.append(arrow)

def level1():
    global drawList,level, startPoint, endPoint
    level = 1
    viz.startLayer(viz.POINTS)
    viz.pointSize(20)
    viz.vertexColor(0,0,1)
    viz.vertex(-3.5,2.0,-9.1)
    viz.vertexColor(0,1,0)
    viz.vertex(-1.5,2.0,-9.1)
    arrow = viz.endLayer()
    drawList.append(arrow)

def clearDrawing():
	while drawList != []:
		drawList.pop().remove()

# tempFlag = 0
# def ontempFlagKeydown():
# 	global tempFlag
# 	if tempFlag==0:
# 		tempFlag = 1
# 	elif tempFlag==1:
# 		tempFlag = 0

# 1. Physical Space to Virtual Space
# 2. Workspace
# 3. Automatic
# 4. Audio 
# 5. Boundary exit entry
# 6. Boundary start recording 
# 7. Metric 
# 8. Time 
# 9. Scoring


# addd a animation path
# timers decrease
# 

# 45 inches 115 cm y-axis 
# 166 cm  x-axis