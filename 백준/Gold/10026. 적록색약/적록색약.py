import sys
sys.setrecursionlimit(100000)
n=int(input())
board=[]
for _ in range(n):
    board.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[0 for _ in range(n)] for _ in range(n)]
rgb=0
rgnb=0

def RGB(x,y):
    visited[x][y]=1
    for i in range(4):
        cx=x+dx[i]
        cy=y+dy[i]
        if 0<=cx<n and 0<=cy<n and visited[cx][cy]==0: #범위내의 안가본 구역이면?
            if board[cx][cy]== board[x][y]:#같은 색상구역이면?
                RGB(cx,cy) #방문처리
for i in range(n):#일반
    for j in range(n):
        if visited[i][j]==0:
            RGB(i,j)
            rgb+=1

visited=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]=="G":
            board[i][j]="R"
for i in range(n):#적록색약
    for j in range(n):
        if visited[i][j]==0:
            RGB(i,j)
            rgnb+=1
print(rgb,rgnb)

