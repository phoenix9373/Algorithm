function solution(m, arr) {
  let i = 0;
  let j = 1;
  let sum = arr[i] + arr[j];
  let cnt = 0;

  while (j < arr.length) {
    if (sum < m) {
      j++;
      if (j < arr.length) sum += arr[j];
    } else if (sum > m) {
      sum -= arr[i];
      i++;
    }

    if (sum === m) {
      cnt++;
      j++;
      if (j < arr.length) sum += arr[j];
    }
  }

  return cnt;
}

let a = [1, 2, 1, 3, 1, 1, 1, 2];
console.log(solution(6, a));
