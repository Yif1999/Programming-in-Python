a,b=input().split()
a,b=int(a),int(b)
count=0
for i in range(a,b+1):
  if i%3==0 and i%5==0 and i%7==0:
    count+=1
print(count)