import heapq
n,k=map(int,input().split())
j=[]
for _ in range(n):
    m,v=map(int,input().split())
    heapq.heappush(j,(m,v))
bag=[]
for _ in range(k):
    heapq.heappush(bag,int(input()))

inbag=[]
total=0
for _ in range(k):
    currentbag=heapq.heappop(bag)
    while j and currentbag>=j[0][0]:
        [m,v]=heapq.heappop(j)
        heapq.heappush(inbag,-v)
    if inbag:
        total-=heapq.heappop(inbag)
    elif not j:
        break
print(total)

