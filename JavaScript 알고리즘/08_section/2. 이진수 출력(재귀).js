function solution(n) {
  let answer = "";

  function dfs(n) {
    if (n === 0) {
      return;
    }

    dfs(parseInt(n / 2));
    answer += String(n % 2);
  }

  dfs(n);

  return answer;
}

console.log(solution(13));
