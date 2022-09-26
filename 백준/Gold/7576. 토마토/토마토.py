from collections import deque
import queue

m,n=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

ans=0

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not board[nx][ny]:
                    queue.append((nx,ny))
                    board[nx][ny]=board[x][y]+1
    return board

queue=deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))
bfs()

if all(0 not in l for l in board):
    print(max(map(max,board))-1)
else:
    print(-1)


