function solution(n) {
  let answer = "";

  function dfs(n) {
    if (n > 7) return;

    dfs(n * 2);
    dfs(n * 2 + 1);
    answer += String(n);
  }

  dfs(n);

  return answer;
}

console.log(solution(1));
