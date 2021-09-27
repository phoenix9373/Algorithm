function solution(s) {
  let answer = "";
  let res = [];
  for (const c of s) {
    if (!res.includes(c)) res.push(c);
  }
  answer = res.join("");
  return answer;
}
console.log(solution("ksekkset"));
