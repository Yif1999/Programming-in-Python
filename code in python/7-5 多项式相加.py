fx=input().split(', ')
gx=input().split(', ')
exp=int(input())
px={}
for i in fx+gx:
  i=i.split(' ')
  k=int(i[1]);v=int(i[0])
  if k in px:
    px[k]+=v
  else:
    px[k]=v
print(px.get(exp,0))