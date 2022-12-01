def solution(N, stages):
    answer = []
    challenger=len(stages)
    for current_level in range(1,N+1):
        cnt=stages.count(current_level)
        if challenger==0:
            answer.append([current_level,0])
        else:
            answer.append([current_level,(cnt/challenger)])
        challenger-=cnt
    answer.sort(reverse=True, key=lambda x:x[1])
    answer=[i[0]for i in answer]
    return answer