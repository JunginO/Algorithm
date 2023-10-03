def solution(nums):
    answer = 0
    available_choice=len(nums)/2
    res = len(list(set(nums)))
    if available_choice < res:
        answer = available_choice
    else:
        answer = res
    
    return answer