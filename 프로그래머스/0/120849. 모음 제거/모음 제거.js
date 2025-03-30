function solution(my_string) {
    let alpha = ['a', 'e', 'i', 'o', 'u' ];
    let answer = [];
    let strArr = my_string.split('');
    for (let i = 0; i<= my_string.length; i++) {
        if(!alpha.includes(strArr[i])) {
            answer.push(strArr[i]);
        }
    }
    return answer.join('');
}