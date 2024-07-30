def solution(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = []
    
    for i in s:
        if i == " ":
            result.append(" ")
        elif i.islower():
            new_index = lower_list.find(i) + n
            result.append(lower_list[new_index % 26])
        else:
            new_index = upper_list.find(i) + n
            result.append(upper_list[new_index % 26])
            
    return "".join(result)
