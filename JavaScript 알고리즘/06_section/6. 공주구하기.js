function solution(n, k) {
  // 1. check: 숫자값을 가진 Array
  const check = Array.from({ length: n }, (_, i) => i + 1);

  // 2. 반복문을 돌면서 k 값의 배수이면 추출.
  let i = 0;
  let cnt = 0;

  while (check.length > 1) {
    // 해당 번호
    cnt++;

    // k번째인지 check
    if (cnt === k) {
      check.splice(i, 1);
      cnt = 0;
    } else {
      i = (i + 1) % check.length;
    }
  }

  return check.pop();
}

console.log(solution(7, 3));
