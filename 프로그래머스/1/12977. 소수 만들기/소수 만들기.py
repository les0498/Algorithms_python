from itertools import combinations

def isPrime(n):
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True
    

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))
    for arr in cmb:
        if isPrime(sum(arr)):
            answer += 1 
    return answer 
