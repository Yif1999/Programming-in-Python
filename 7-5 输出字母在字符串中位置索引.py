s=input()
sr=s[::-1]
find=input().split()
n=len(s)-1
for i in sr:
  if i in find:
    print('{} {}'.format(n,s[n]))
  n-=1