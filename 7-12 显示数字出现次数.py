dnum=int(input())
hnum=hex(dnum).replace('0x','')
fnum=input()
count=0
for i in hnum:
  if i==fnum:
    count+=1
print(count)