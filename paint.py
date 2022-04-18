import vizmat, viz, vizact
from levelsHello import *

# def getPos():
#     global fastrak1
#     print(fastrak1.getPosition())
#     return fastrak1.getPosition()
collectionList = []
flag = 0
def addArrow(begin,end):
    ARROW_SIZE = 0.015
	#Find distance between points
    d = vizmat.Distance(begin,end)
    #if tempFlag == 1:
    begin[2] = -9.1 
    end[2] = -9.1
	#Draw arrow line
    viz.startlayer(viz.LINES)
    viz.linewidth(8)
    viz.vertex(begin)
    viz.vertex(end)
    arrow = viz.endlayer()
    return arrow

l = getPos()
arrow1 = addArrow(l,l)
arrow1.color(viz.GREEN)
prevR = l
r = l

def update():
    global l,r,prevR,prevTime,collectionList,drawList,flag
    l = getPos()
    r = l
    r[0] = r[0]*10 
    r[1] = -r[1]*10
    r[2] = r[2]*10
    print(r)
    arrow1 = addArrow(prevR,r)
    arrow1.color(viz.GREEN)
    drawList.append(arrow1)
    # print('IamFlag', flag)
    if flag==1:
        collectionList.append(r)
    prevR = r
    print("YES")




