def solution(k, tangerine):
    answer = 0 
    
    d = {} 
    for i in tangerine: 
        if (i in d):
            d[i] += 1 
        else: 
            d[i] = 1
    d = sorted(d.items(), key = lambda x: x[1], reverse = True )
    
    total = 0
    for size, count in d: 
        total += count 
        answer += 1 
        if total >= k:
            break
            
    return answer