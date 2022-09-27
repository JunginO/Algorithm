from collections import deque

n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs(a,b,k):
    queue.append((a,b))
    visited[a][b]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]==0 and board[nx][ny]>k:
                    queue.append((nx,ny))
                    visited[nx][ny]=+1
    return visited


highest=max(map(max,board))
ans=[]
for k in range(highest+1):
    current=0
    queue=deque()
    visited=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]>k and visited[i][j]==0:
                bfs(i,j,k)
                current+=1
    ans.append(current)
print(max(ans))