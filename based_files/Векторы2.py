from random import randint
from math import sqrt
x1, y1, z1, x2, y2, z2 = map(int, input().split())
print(sqrt((max(x1,x2)-min(x1,x2))**2 + (max(y1,y2)-min(y1,y2))**2 + (max(z1,z2)-min(z1,z2))**2))
