function solution(m, arr) {
  let i = 0;
  let j = 0;
  let cnt = 0;
  let sum;

  while (i < arr.length) {
    if (i === j) {
      sum = arr[i];
    }

    if (sum > m) {
      i++;
      j = i;
    }

    while (sum <= m) {
      cnt++;
      j++;
      if (j < arr.length) sum += arr[j];
      if (j >= arr.length) {
        i++;
        j = i;
        break;
      }
    }
  }

  return cnt;
}

let a = [1, 3, 1, 2, 3];
console.log(solution(5, a));
