dim=int(input())
mat=[]
for i in range(dim):
  mat.append(list(map(int,input().split())))
count=0
for row in mat:
  column=0
  for i in row:
    if i==max(row) and i==min(list(mat[r][column] for r in range(dim))):
      count+=1
    column+=1
print(count)