function solution(m, arr) {
  // N개 중 M개 출력
  // 순서대로 나열
  const answer = [];
  const visited = Array.from({ length: arr.length }, () => 0);
  const tmp = Array.from({ length: m }, () => 0);

  function dfs(curr) {
    if (curr === m) {
      answer.push(tmp.slice());
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (visited[i] === 0) {
        tmp[curr] = arr[i];
        visited[i] = 1;
        dfs(curr + 1);
        visited[i] = 0;
      }
    }
  }

  dfs(0);

  return answer;
}

let arr = [3, 6, 9];
console.log(solution(2, arr));
