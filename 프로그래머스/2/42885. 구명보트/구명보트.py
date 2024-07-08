from collections import deque

def solution(people, limit):
    answer = 0 
    people = deque(sorted(people))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft() 
        else: 
            answer += 1 
            people.pop() # 가장 무거운 사람 제거
    if people : 
        answer+= 1 
    
    return answer 