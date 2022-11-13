from collections import deque
n,m,k,x=map(int,input().split())
lst=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)

length=[-1 for _ in range(n+1)]
q=deque()
q.append(x)
length[x]=0
while q:
    current=q.popleft()
    for i in lst[current]:#연결된 노드 하나씩 확인
        if length[i]==-1:#방문안한곳이면
            length[i]=length[current]+1#현재거리+1
            q.append(i)#큐에 넣어준다

ans=[]
for i in range(len(length)):
    if length[i]==k:
        ans.append(i)
        
if len(ans)==0:
    print(-1)
else:
    for i in ans:
        print(i)

