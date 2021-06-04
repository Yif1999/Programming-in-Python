l=input().split()
dict={}
for a in l[1:]:
  if a in dict.keys():
    dict[a]+=1
  else:
    dict[a]=1
ans=max(dict.items(), key=lambda x:x[1])
print(str(ans[0])+' '+str(ans[1]))