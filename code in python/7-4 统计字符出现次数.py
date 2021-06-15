str=input()
count={}
for i in str:
  if i in count:
    count[i]+=1
  else:
    count.update({i:1})
find=input()
if find in count:
  print(count[find])
else:
  print('0')