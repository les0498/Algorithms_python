function solution(numbers) {
    var answer = 0;
    let gap = 0;
    for (let i = 0; i < numbers.length; i++) {
        gap += numbers[i] ; 
        answer = gap / numbers.length; 
    }
    return answer;
}