def solution(x, n):
    answer = []
    for i in range(1,n+1):
        i = x*i
        answer.append(i)
    return answer