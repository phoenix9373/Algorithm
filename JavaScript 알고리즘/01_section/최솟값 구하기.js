function solution(arr) {
  let answer,
    min = Number.MAX_SAFE_INTEGER;
  for (const v of arr) {
    if (v < min) min = v;
  }
  answer = min;
  return answer;
}

function solution2(arr) {
  let answer = Math.min(...arr);
  return answer;
}

let arr = [5, 7, 1, 3, 2, 9, 11];
console.log(solution(arr));
