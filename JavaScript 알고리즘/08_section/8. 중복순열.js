function solution(n, m) {
  // n: 1부터 n
  // m: 중복추출

  const answer = [];

  function comb(depth, res = []) {
    if (depth === m) {
      answer.push(res.join(" "));
      return;
    }

    for (let i = 1; i < n + 1; i++) {
      comb(depth + 1, [...res, i]);
    }
  }

  comb(0);

  return [answer, answer.length];
}

console.log(solution(3, 2));
