lst=list(map(int,input()))
half=int(len(lst)/2)
left=0
right=0
for i in range(half):
    left+=lst[i]
for i in range(half):
    right+=lst[half+i]
if left==right:
    print("LUCKY")
else:
    print("READY")