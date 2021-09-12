function solution(a, b, c) {
  let answer = "YES",
    max;

  if (a > b) max = a;
  else max = b;
  if (c > max) max = c;
  if (a + b + c >= 2 * max) answer = "NO";

  return answer;
}

console.log(solution(13, 33, 17));
