def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        ary = array[commands[i][0]-1:commands[i][1]]
        ary.sort()
        answer.append(ary[commands[i][2]-1])
        
    return answer