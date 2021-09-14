function solution(arr) {
  let answer;
  let prev;

  arr = arr.map((a, i) => [a, i]);
  arr.sort((a, b) => b[0] - a[0]);

  for (let i = 0; i < arr.length; i++) {
    if (prev && prev === arr[i][0]) arr[i].push(arr[i - 1][2]);
    else arr[i].push(i + 1);
    prev = arr[i][0];
  }

  arr.sort((a, b) => a[1] - b[1]);

  answer = arr.map((a) => a[2]);

  return answer.join(" ");
}

let arr = [87, 89, 92, 100, 76];
console.log(solution(arr));
