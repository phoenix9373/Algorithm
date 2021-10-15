function solution(n) {
  if (n === 1) return [1];

  const arr = solution(n - 1);

  return [...arr, n];
}

const testcase = {
  n: 5,
};
console.log(solution(testcase.n).join(" "));
