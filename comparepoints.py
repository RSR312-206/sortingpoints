#in this piece of code, I am attempting to compare points and order them from least to greatest. 
#what do I need? array, point class, functions, nested loops. 

import copy 

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) +"," + str(self.y) + ")" 

    def compare(self, other):
        if self.x == other.x and self.y == other.y:
            return 0
        elif other.y > self.y:
            return -1
        elif other.y < self.y:
            return 1 

p = Point(0,1)
p2 = Point(-2,4)
p3 = Point(-1, -1)
p4 = Point(2, -8)
points = [p, p2, p3, p4]

print str(p2) 

print p.compare(p2)

print points
        
class PointList:

    def __init__(self, points):
        self.points = points
# i want logic as to how to print out the point- use str
    def __str__(self):
        res = "" 
        for i in range(len(self.points)):
            res += str(self.points[i])
        return res 

    
    def sort(self):
        if len(self.points) == 0:
            return self
        else: 
            for i in range(len(self.points)):
                for j in range(len(self.points)):
                    current = self.points[i] 
                    next = self.points[j]
                    if current.compare(next) == -1:
                        temp = current
                        self.points[i] = next
                        self.points[j] = temp 


               
        return self

point_list = PointList(points) 

print str(point_list)  
print str(point_list.sort())






               
            






                
            


