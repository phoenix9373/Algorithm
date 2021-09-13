function solution(s) {
  let answer = "";
  for (const c of s) {
    if (c === c.toUpperCase()) answer += c.toLowerCase();
    else answer += c.toUpperCase();
  }
  return answer;
}

console.log(solution("StuDY"));
