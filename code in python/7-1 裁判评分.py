n=int(input())
score=list(map(int,(input().split())))
score.remove(max(score))
score.remove(min(score))
print("{:.2f}".format(sum(score)/(n-2)))