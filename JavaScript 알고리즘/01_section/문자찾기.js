function solution(s, t) {
  let answer = 0;
  for (const k of s) {
    if (k === t) answer++;
  }
  return answer;
}

let str = "COMPUTERPROGRAMMING";
console.log(solution(str, "R"));
