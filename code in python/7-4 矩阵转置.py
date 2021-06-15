r,c=input().split()
r,c=int(r),int(c)
mat=[]
for i in range(r):
  mat.append(list(map(int,input().split())))
for i in range(c):
  outLine=list(str(mat[j][i]) for j in range(r))
  print(' '.join(outLine))