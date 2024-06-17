def solution(a, b, n):
    answer = 0
    while n >= a:
        newCount = n // a * b
        answer += newCount
        n = n % a + newCount
    return answer