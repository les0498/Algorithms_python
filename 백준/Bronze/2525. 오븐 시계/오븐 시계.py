Current_time = input().split(' ')
H = int(Current_time[0])
M = int(Current_time[1])

need_time = int(input()) 

H += need_time // 60
M += need_time % 60

if M >= 60:
  M -= 60 
  H += 1 
if H >= 24: 
   H -= 24
    
print(str(H)+" "+str(M))
