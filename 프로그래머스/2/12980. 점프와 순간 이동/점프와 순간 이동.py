def solution(N):
    answer = 0
    while N > 0:
        if N % 2 == 0:
            N = N //2
        else: 
            N = N - 1
            answer += 1
    return answer 

        
