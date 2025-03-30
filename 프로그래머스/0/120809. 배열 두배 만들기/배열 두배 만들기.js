function solution(numbers) {
    var answer = [];
    let gap = 0;
    for (let i = 0 ; i < numbers.length; i++) {
        gap = numbers[i] * 2; 
        answer.push(gap);
    }
    return answer;
}