x=eval(input())
if x!=0:
  y=1/x
  print("f({0})={1:.3f}".format(x,y))
else:
  y=0
  print("f({0:.1f})={1:.3f}".format(x,y))