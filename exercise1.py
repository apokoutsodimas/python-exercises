import random
from PIL import Image, ImageDraw
import operator
from random import randint
#Point Class,
class Point:
    #constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y
#Circle Class
class Circle(object):
    #constructor
    def __init__(self,p,r):
        self.center=p
        self.r=r
    #check if intersects with another cycle
    #Two circles intersect if, and only if, the distance between their centers is between the sum and the difference of their radii.
    def Intersects(self,c2):
        if ((self.r-c2.r)^2<=(self.center.x-c2.center.x)^2+(self.center.y-c2.center.y)^2) and ((self.center.x-c2.center.x)^2+(self.center.y-c2.center.y)^2<=(self.r+c2.r)^2):
            return True
        else:
            return False

#find Intersected circles
def findIntersected(designedcircles):
    intersected=[]
    for i in range(0,20-1):
        for j in range (i+1,20):
            isintersected=designedcircles[i].Intersects(designedcircles[j])
            if (isintersected):
                #mark as intesected both circles
                intersected.append(i)
                intersected.append(j)
    #remove duplicates
    trueinter=list(set(intersected))
    return len(trueinter)


def drawCircles(designedcircles):
    im = Image.new("RGB", (1024, 1024), "white")
    draw = ImageDraw.Draw(im)
    for i in range(0,20):
        draw.ellipse((designedcircles[i].center.x-designedcircles[i].r, designedcircles[i].center.y-designedcircles[i].r, designedcircles[i].center.x+designedcircles[i].r, designedcircles[i].center.y+designedcircles[i].r), outline ='red')
    im.show()
    im.save("exercise1.png","PNG")

def main():
    #random radius
    radius = random.sample(range(10,500),20)
    #limits for circles' centers, so as to be within the canvas
    lowerx=radius
    upperx=list(map(operator.sub, [1024]*20, radius))
    lowery=radius
    uppery=list(map(operator.sub, [1024]*20, radius))
    pointx=[]
    pointy=[]

    for i in range(0,20):
        pointx.append(randint(lowerx[i],upperx[i]))
        pointy.append(randint(lowery[i],uppery[i]))
    designedcircles=[]
    #construct centers of circles
    for i in range(0, 20):
        center = Point(pointx[i],pointy[i])
        designedcircles.append(Circle(center,radius[i]))

    num = findIntersected(designedcircles)
    print('The number of intersected nodes is: %d' %num)

    drawCircles(designedcircles)

if __name__ == '__main__':
    main()










