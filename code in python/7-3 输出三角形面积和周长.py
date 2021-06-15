import math

a=input().split()
b=list(map(int,a))
b.sort()
if b[0]+b[1]>b[2]:
  s=(sum(b))/2
  area= math.sqrt(s*(s-b[0])*(s-b[1])*(s-b[2]))
  print("area = {0:.2f}; perimeter = {1:.2f}".format(area,sum(b)))
else:
  print("These sides do not correspond to a valid triangle")