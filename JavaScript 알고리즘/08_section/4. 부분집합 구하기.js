function solution(n) {
  const answer = [];
  const initial = Array.from({ length: n }, (_, i) => i + 1);

  function dfs(curr, cum = []) {
    if (curr === initial.length) {
      answer.push(cum.join(" "));
      return;
    }

    dfs(curr + 1, [...cum, initial[curr]]);
    dfs(curr + 1, cum);
  }

  dfs(0);

  return answer;
}

console.log(solution(3));
