def solution(s):
    answer = s.lower()
    p = answer.count("p")
    y = answer.count("y")
    if p == y :
        return True 
    elif p == 0 and y == 0 : 
        return True 
    else :
        return False 
