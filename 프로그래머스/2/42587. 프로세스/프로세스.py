from collections import deque
def solution(priorities, location):
    q_prior = deque(priorities)
    q_idx = deque(range(len(priorities)))
    
    order = 0
    
    while q_prior:
        p = q_prior.popleft()
        i = q_idx.popleft()
        
        if q_prior and p < max(q_prior):
            q_prior.append(p)
            q_idx.append(i)
        else: 
            order += 1
            if i == location:
                return order