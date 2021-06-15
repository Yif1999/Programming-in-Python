n=int(input())
monkey=list(map(int,list(range(1,n+1))))
count=0
while len(monkey)!=1:
  rmv=[]
  for i in monkey:
    count+=1
    if count%3==0:
      rmv.append(i)
  for j in rmv:
    monkey.remove(j)
print(monkey[0])