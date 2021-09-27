function solution(arr) {
  let answer = 0,
    max = Number.MIN_SAFE_INTEGER;
  for (const k of arr) {
    if (k > max) {
      max = k;
      answer++;
    }
  }
  return answer;
}

let arr = [130, 135, 148, 140, 145, 150, 150, 153];
console.log(solution(arr));
