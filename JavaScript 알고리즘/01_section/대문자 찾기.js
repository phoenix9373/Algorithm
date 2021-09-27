function solution(s) {
  let answer = 0;
  for (const c of s) {
    let tmp = c.toUpperCase();
    if (tmp === c) answer++;
  }
  return answer;
}

let str = "KoreaTimeGood";
console.log(solution(str));
