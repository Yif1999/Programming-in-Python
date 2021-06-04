r,c=input().split()
r,c=int(r),int(c)
mat=[]
for i in range(r):
  mat.append(list(map(int,input().split())))
none=1
for i in range(1,r-1):
  for j in range(1,c-1):
    if mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i][j+1]:
      print(mat[i][j],i+1,j+1)
      none=0
if none:
  print(None,r,c)