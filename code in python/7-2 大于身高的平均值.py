shenGao=list(map(int,list(input().split())))
av=sum(shenGao)/len(shenGao)
first=1
for i in shenGao:
  if i > av :
    print(str(i)+' ',end='')