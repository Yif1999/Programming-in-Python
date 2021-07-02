[n,digit]=(input().split())
n=int(n);digit=int(digit)

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print(digit,end=' ')
        else:
            print(digit-1,end=' ')
    print()
