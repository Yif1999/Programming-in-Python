M,N=input().split()
M=int(M);N=int(N)
dividend=max(M,N)
divisor=min(M,N)
while dividend%divisor!=0:
  divisor,dividend=dividend%divisor,divisor
max_YueShu=divisor
min_BeiShu=M*N/max_YueShu
print(max_YueShu,int(min_BeiShu))