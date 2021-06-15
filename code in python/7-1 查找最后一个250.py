numList=input().split()
index=0
count=1
for i in numList:
  if i=='250':
    index=count
  count+=1
print(index)