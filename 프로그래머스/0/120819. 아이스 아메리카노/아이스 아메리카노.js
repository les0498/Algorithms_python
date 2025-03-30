function solution(money) {
    const americano = 5500;
    let gap = Math.floor(money / americano);
    let change = money % americano ; 
    let answer = [gap,change];
    return answer;
}