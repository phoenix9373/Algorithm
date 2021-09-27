function solution(s) {
  let answer = "",
    max = Number.MIN_SAFE_INTEGER;
  for (const w of s) {
    if (w.length > max) {
      max = w.length;
      answer = w;
    }
  }
  return answer;
}

let str = ["teacher", "time", "student", "beautiful", "good"];
console.log(solution(str));
