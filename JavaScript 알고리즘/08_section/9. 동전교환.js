function solution(m, arr) {
  // m: 거슬러 줄 돈
  // arr: 동전 배열

  let answer = 0;

  function change(curr, rest) {
    if (rest === 0) return;

    while (rest >= arr[curr]) {
      rest -= arr[curr];
      answer++;
    }

    change(curr - 1, rest);
  }

  change(arr.length - 1, m);

  return answer;
}

let arr = [1, 2, 5];
console.log(solution(19, arr));
