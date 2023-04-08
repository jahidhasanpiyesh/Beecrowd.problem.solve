# beecrowd problem BE-1015
# solve this problem
# call this math
import math
# convert this item floating numbers
x1,y1=map(float,input().split()) # convert this item floating numbers
x2,y2=map(float,input().split())
# use to math.sqrt() and pow()
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("%0.4f"%distance)