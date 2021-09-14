function solution(arr) {
  let answer = 0,
    cnt = 1;
  for (const k of arr) {
    if (k === 1) {
      answer += cnt;
      cnt++;
    } else {
      cnt = 1;
    }
  }
  return answer;
}

let arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(arr));
