function solution(n) {
    var answer = 0;
    if(n % 7 == 0) {
        return answer = n / 7;
    } else {
        return answer = Math.floor(n / 7) + 1;   
    }
}