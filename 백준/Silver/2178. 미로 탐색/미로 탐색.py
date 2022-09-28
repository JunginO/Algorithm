from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
n,m=map(int,input().split())
board=[]
visited=[[0 for _ in range(m)]for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            if 0<=cx<n and 0<=cy<m:
                if board[cx][cy]!=0 and visited[cx][cy]==0:
                    visited[cx][cy]=1
                    board[cx][cy]=board[x][y]+1
                    queue.append((cx,cy))

queue.append((0,0))
bfs()
print(board[n-1][m-1])