function solution(m, ps, pt) {
  // ps: 점수
  // pt: 시간
  // m: 제한시간

  let answer = Number.MIN_SAFE_INTEGER;

  function dfs(curr, cumScore, cumTime) {
    if (cumTime > m) return;
    if (curr === ps.length) {
      answer = Math.max(answer, cumScore);
      return;
    }

    dfs(curr + 1, cumScore + ps[curr], cumTime + pt[curr]);
    dfs(curr + 1, cumScore, cumTime);
  }

  dfs(0, 0, 0);

  return answer;
}

let ps = [10, 25, 15, 6, 7];
let pt = [5, 12, 8, 3, 4];
console.log(solution(20, ps, pt));
