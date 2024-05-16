def solution(s):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in dic :
        if i in s :
            idx = str(dic.index(i))
            s = s.replace(i, idx)
    answer = int(s)
    return answer