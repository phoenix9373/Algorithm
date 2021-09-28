function solution(m, product) {
  const n = product.length;

  let answer = 0;
  let total = 0;

  product.sort((a, b) => a[0] - b[0]);

  for (const pd of product) {
    total += pd[0] + pd[1];

    const subtotal = total - pd[0] / 2;

    if (subtotal <= m) {
      answer++;
    } else {
      total -= pd[0] + pd[1];
    }
  }

  return answer;
}

let arr = [
  [6, 6],
  [2, 2],
  [4, 3],
  [4, 5],
  [10, 3],
];
console.log(solution(28, arr));
