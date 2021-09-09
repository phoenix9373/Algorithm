function solution(n) {
  let res = 0;

  for (let i = 1; i < n; i++) {
    const check = isValid(i);
    if (check === 1 && res < i) res = i;
  }

  return res;
}

function isValid(x) {
  const str1 = x.toString(10); // 625
  const l = str1.length; // 3

  const str2 = (x * x).toString(10); // 390625
  if (str2.slice(-l) === str1) return 1;
  return 0;
}

console.log(solution(1000));
