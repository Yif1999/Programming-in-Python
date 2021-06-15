n=int(input())
mat=[]
for i in range(n):
  mat.append(list(map(float,input().split())))
zhuduijiao=list(mat[i][i] for i in range(n))
fuduijiao=list(mat[i][n-i-1] for i in range(n))
if n%2==1 :
  fuduijiao.remove(mat[n//2][n//2])
Sum=sum(zhuduijiao)+sum(fuduijiao)
print('{:.2f}'.format(Sum))