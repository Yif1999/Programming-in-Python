def fn(a,n):
  Sum=0
  for i in range(1,n+1):
    Sum+=int(str(a)*i)
  return Sum

a,b=input().split()
s=fn(int(a),int(b))
print(s)