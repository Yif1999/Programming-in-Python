n=int(input())
graph={}
for i in range(n):
  graph.update(eval(input()))
point=n
edge=0
length=0
for dic in graph:
  edge+=len(graph[dic])
  for weight in graph[dic]:
    length+=int(graph[dic][weight])
print(point,edge,length)