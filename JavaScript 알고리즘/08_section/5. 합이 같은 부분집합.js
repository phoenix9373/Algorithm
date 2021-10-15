function solution(arr) {
  let answer = "NO";

  function dfs(curr, selected = [], notSelected = []) {
    if (answer === "YES") return;
    if (curr === arr.length) {
      const prevGroupSum = selected.reduce((acc, cur) => acc + arr[cur], 0);
      const nextGroupSum = notSelected.reduce((acc, cur) => acc + arr[cur], 0);

      if (prevGroupSum === nextGroupSum) answer = "YES";
      return;
    }

    dfs(curr + 1, [...selected, curr], notSelected);
    dfs(curr + 1, selected, [...notSelected, curr]);
  }

  dfs(0);

  return answer;
}

const a = [1, 3, 10];
console.log(solution(a));
