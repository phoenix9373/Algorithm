function solution(arr) {
  let answer = [],
    sum = 0,
    min = Number.MAX_SAFE_INTEGER;
  for (const v of arr) {
    if (v % 2 === 1) {
      sum += v;
      if (min > v) min = v;
    }
  }
  console.log(sum);
  console.log(min);
  return answer;
}

arr = [12, 77, 38, 41, 53, 92, 85];
solution(arr);
