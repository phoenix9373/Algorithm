// d(n) = n + n % 10 + n % 100 + ...
// 39 = 33 + 3 + 3

function solution(k) {
  const res = Array.from({ length: k }, () => 0);

  // 생성자
  for (let i = 1; i <= k; i++) {
    if (d(i) <= 10000) res[d(i)] = 1;
  }

  for (let i = 1; i < k; i++) {
    if (res[i] === 0) console.log(i);
  }
}

function d(n) {
  let res = n;

  while (n > 0) {
    let quo = parseInt(n / 10);
    let div = n % 10;

    res += div;
    n = quo;
  }

  return res;
}

solution(10000);
