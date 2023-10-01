def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in lost[:]:
        #lost랑reserve 중복 있음? -> 대여 불가, reserve와 lost에서 제거
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    print(reserve,lost)
    cplost=lost.copy()
    for i in lost:
        if i-1 in reserve:
            cplost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            cplost.remove(i)
            reserve.remove(i+1)
    answer = n-len(cplost)
    #lost의 경우 1번부터 reserve에서 구제 가능한지 체크
    #1 -> 2, 2->1,3 ,3-> 2,4, 4->3,5 중에 reserve 있는지 체크, 있을 경우 lost와 reserve에서 동시에 제거
    #5에서 lost에 남아있는 갯수를 뺀걸 return
    return answer