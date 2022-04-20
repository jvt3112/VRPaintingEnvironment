import numpy as np

def getDistance(listOfPoints):
    length = 0 
    listOfPoints = np.array(listOfPoints)
    for i in range(1,len(listOfPoints)):
        length += np.linalg.norm(listOfPoints[i]- listOfPoints[i-1])
    return length

def circleClearCheck(pointList, threshold, centre, originalPerimeter, r=1):
	for point in pointList:
			dist = np.linalg.norm(point-centre)
			if dist<r-threshold and dist>r+threshold:
					return False
	perimeter = getDistance(pointList)
	
	if perimeter<originalPerimeter+threshold and perimeter>originalPerimeter-threshold:
		return True,(1-abs(perimeter-originalPerimeter)/(originalPerimeter*2))*100
	else:
		return False,None

def lineClearCheck(listOfPoints, threshold, originalLength=2):
    print(listOfPoints, 'HelloIamList')
    for point in listOfPoints:
        if point[0] < (-1) and point[0] > (-4) and point[1] < 2.5 and point[1] > 1.5:
            pass
        else:
            return False,None
    perimeter = getDistance(listOfPoints)
    if perimeter<originalLength+threshold and perimeter>originalLength-threshold:
        return True,(1-abs(perimeter-originalLength)/(originalLength*2))*100
    else:
        return False,None

def squareClearCheck(pointList, threshold, checkPointList, originalPerimeter=8):
	# checkPointList : left,right,top,bottom
	print(pointList, 'HelloIamList')
	left,right,top,bottom = checkPointList
	for i in range(len(pointList)):
			perp1 = abs(left-pointList[i][0])
			perp2 = abs(right-pointList[i][0])
			perp3 = abs(top-pointList[i][1])
			perp4 = abs(bottom-pointList[i][1])
			allPerp = [perp1,perp2,perp3,perp4]
			index = allPerp.index(min(allPerp))
			print(allPerp, index)
			if index==0:
					if perp1>threshold:
							return False, None
			elif index==1:
					if perp2>threshold:
							return False, None
			elif index==2:
					if perp3>threshold:
							return False, None
			elif index==3:
					if perp4>threshold:
							return False, None
	perimeter = getDistance(pointList)
	if perimeter<originalPerimeter+threshold and perimeter>originalPerimeter-threshold:
		return True, (1-abs(perimeter-originalPerimeter)/(originalPerimeter*2))*100
	else:
		return False, None

