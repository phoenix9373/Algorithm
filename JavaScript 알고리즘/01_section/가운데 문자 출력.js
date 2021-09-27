function solution(s) {
  let answer;
  let mid = Math.floor(s.length / 2);
  if (s.length % 2 !== 0) {
    answer = s.charAt(mid);
  } else {
    answer = s.slice(mid - 1, mid + 1);
  }
  return answer;
}
console.log(solution("good"));
