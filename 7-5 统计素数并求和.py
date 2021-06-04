m,n=map(int,input().split())
count=0
add=0
for i in range(m,n+1):
  isSuShu=1
  if i==1:
    isSuShu=0
  for j in range(2,i):
    if i%j ==0:
      isSuShu=0
      break
  if isSuShu:
    count+=1
    add+=i
print(count,add)