n=int(input())
lst=[]
for i in range(n):
  lst.append(input().split())
while len(lst)>0:
  for i in range(len(lst)-1,0,-1):
    if lst[i][0]!=lst[0][0]:
      print(lst[0][1],lst[i][1])
      lst.remove(lst[i])
      lst.remove(lst[0])
      break