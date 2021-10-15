function solution(c, arr) {
  // C: 제한사항, 이하 조건
  // arr: 바둑이의 몸무게 배열

  let max = 0;

  function dfs(curr, selected = []) {
    if (curr === arr.length) {
      const sum = selected.reduce((a, b) => a + arr[b], 0);

      if (sum > max && sum < c) max = sum;

      return;
    }

    dfs(curr + 1, [...selected, curr]);
    dfs(curr + 1, selected);
  }

  dfs(0);

  return max;
}

let arr = [81, 58, 42, 33, 61];
console.log(solution(259, arr));
