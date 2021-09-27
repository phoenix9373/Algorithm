function solution(s) {
  let answer = "";
  for (const c of s) {
    answer += c.toUpperCase();
  }
  return answer;
}

let str = "ItisTimeToStudy";
console.log(solution(str));
