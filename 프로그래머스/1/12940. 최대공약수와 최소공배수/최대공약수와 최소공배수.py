import math 

def solution(n,m):
    answer = [] 
    gcd_n = math.gcd(n, m)
    answer.append(gcd_n)
    lcd = (n*m) // gcd_n
    answer.append(lcd) 
    
    return answer 