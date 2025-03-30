function solution(slice, n) {
    answer = 0;
    if (n%slice == 0) {
        return answer = n / slice;
    } else {
        return answer = Math.floor(n / slice) + 1;
    }
}