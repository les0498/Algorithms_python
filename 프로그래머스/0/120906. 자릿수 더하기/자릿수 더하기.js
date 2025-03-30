function solution(n) {
    var answer = 0;
    let m = String(n); 
    for (let i=0; i<m.length; i++) {
        answer += Number(m[i]);
    }
    return answer;
}