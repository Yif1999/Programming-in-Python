N=int(input())
age=list(map(int,input().split()))
dic={}
for i in age:
  dic[i]=dic.get(i,0)+1
lst=list(dic.items())
lst.sort(key=lambda x:x[0])
for res in lst:
  if res[1]!=0:
    print('{0}:{1}'.format(res[0],res[1]))