const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

const number = parseInt(input);

function solution(n) {
  let res = 0;

  for (let i = 1; i <= n; i++) {
    if (check(i)) res++;
  }

  return res;
}

function check(n) {
  let res = [];
  let diff, prev;

  while (n > 0) {
    res.push(n % 10);
    n = parseInt(n / 10);
  }

  for (const k of res) {
    if ((diff || diff === 0) && k - prev !== diff) return false;
    if (prev || prev === 0) diff = k - prev;
    prev = k;
  }

  return true;
}

console.log(solution(number));
