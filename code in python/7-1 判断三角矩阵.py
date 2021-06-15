n=int(input())
for k in range(n):
  dim=int(input())
  mat=[]
  for i in range(dim):
    mat.append(list(map(int,input().split())))
  upper,lower=1,1
  for r in range(dim):
    for c in range(r+1,dim):
      if mat[r][c]:
        lower=0
    for c in range(r):
      if mat[r][c]:
        upper=0
  if upper:
    print('upper triangular matrix')
  elif lower:
    print('lower triangular matrix')
  else:
    print('no')