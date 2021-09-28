const log = console.log;

function solution(n, k, card) {
  let answer;

  const comb = getComb(card, k).map(
    (arr) => arr.reduce((acc, cur) => acc + cur),
    0
  );

  comb.sort((a, b) => b - a);

  let prev = -1;
  let count = 0;

  for (v of comb) {
    if (prev !== v) count++;
    if (k === count) {
      answer = v;
      break;
    }
    prev = v;
  }

  return answer;
}

function getComb(arr, c) {
  const res = [];
  if (c === 1) return [...arr.map((a) => [a])];

  arr.forEach((v, i, origin) => {
    const rest = origin.slice(i + 1);
    const comb = getComb(rest, c - 1); // 어떤 값?
    res.push(...comb.map((sub) => [v, ...sub]));
  });

  return res;
}

let arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
console.log(solution(10, 3, arr));
