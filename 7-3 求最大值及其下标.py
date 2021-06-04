n=int(input())
l=input().split()
l=list(map(int,l))
mx=max(l)
pos=0
for i in l:
  if i==mx:
    break
  pos+=1
print(str(mx)+' '+str(pos))