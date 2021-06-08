def fact(x):
  if x==0 or x==1:
    return 1
  else:
    return x*fact(x-1)

def funcos(eps,x):
  index=0
  Sum=0
  while True:
    item=x**(index*2)/fact(index*2)
    if item<eps:
      break
    Sum+=(-1)**index*item
    index+=1
  return Sum

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))