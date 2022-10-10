from collections import deque
n=int(input())#보드 크기
k=int(input())#사과갯수
apple=[]
for _ in range(k):
    x,y=map(int,input().split())
    apple.append([x-1,y-1])
cp=[]#방향 바꾸는 포인트
l=int(input())
for _ in range(l):
    x,y=input().split()
    cp.append([int(x)+1,y])
#위오아왼
dx=[-1,0,1,0]
dy=[0,1,0,-1]
direction=1 #처음에 오른쪽으로 가기때문

sec=0
board=[[0 for _ in range(n)] for _ in range(n)]
board[0][0]=1
first=[0,0]
snake=deque([[0,0]])

while True:
    sec+=1
    for i in range(len(cp)):
        if sec==cp[i][0]:
            if cp[i][1]=="D":
                direction=(direction+1)%4
            if cp[i][1]=="L":
                direction=(direction+3)%4
    first[0]=first[0]+dx[direction]
    first[1]=first[1]+dy[direction]
    if 0<=first[0]<n and 0<=first[1]<n and board[first[0]][first[1]]==0:
        snake.append([first[0],first[1]])
        board[first[0]][first[1]]=1
        #보드 범위내거나, 뱀이 없는 칸이거나 하면
        if first not in apple:
            #사과아니면 한칸앞으로
            tmp=snake.popleft()
            board[tmp[0]][tmp[1]]=0
        #사과면 그대로
        else:
            apple.remove(first)
            pass
    else:
        break
   
print(sec)   
    
    


