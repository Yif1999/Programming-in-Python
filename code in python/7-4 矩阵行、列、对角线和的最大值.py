mat=list(map(int,input().split()))
row=[sum(mat[0:3]),sum(mat[3:6]),sum(mat[6:9])]
column=[sum(mat[0::3]),sum(mat[1::3]),sum(mat[2::3])]
duijiao=[sum([mat[0],mat[4],mat[8]]),sum([mat[2],mat[4],mat[6]])]
new_list=row+column+duijiao
print(max(new_list))