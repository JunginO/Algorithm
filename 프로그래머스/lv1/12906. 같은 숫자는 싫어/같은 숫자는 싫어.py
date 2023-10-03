def solution(arr):
    answer = []

    for item in arr:
        if not answer:
            answer.append(item)
        elif item != answer[-1]:
            answer.append(item)
    return answer