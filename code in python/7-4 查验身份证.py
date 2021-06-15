weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
dictionary=['1','0','X','9','8','7','6','5','4','3','2']
n=int(input())
ID=[]
for i in range(n):
   ID.append(input())
error=[]
for i in range(len(ID)):
    count=0
    add=0
    flag=0
    lst=list(ID[i])
    for j in lst:
        if not(48<=ord(j)<=57):
            flag=1
            break
        add=add+int(j)*weight[count]
        count=count+1
        if count==17:
            break
    if flag==1:
        error.append(i)
    else:
        Divide=add%11
        if lst[-1]!=dictionary[Divide]:
            error.append(i)
if len(error)==0:
    print("All passed")
else:
    for i in error:
        print(ID[i])
        