function solution(numbers) {
    var answer = 0;
    let gap = numbers.sort((a, b) => b-a)
    answer = gap[0] * gap[1]
    return answer;
}