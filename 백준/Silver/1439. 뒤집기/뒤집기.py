lst=list(map(int,input()))
cnt=0
for i in range(len(lst)-1):
    if lst[i]!=lst[i+1]: #숫자 바뀌는 지점이면
        cnt+=1
print((cnt+1)//2)