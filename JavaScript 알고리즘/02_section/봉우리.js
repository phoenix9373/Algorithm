function solution(arr) {
  let answer = 0;
  let n = arr.length;

  let di = [0, 0, 1, -1];
  let dj = [1, -1, 0, 0];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      let flag = false;
      for (let k = 0; k < 4; k++) {
        let ni = i + di[k];
        let nj = j + dj[k];

        if (ni >= n || nj >= n || ni < 0 || nj < 0) continue;

        if (arr[i][j] <= arr[ni][nj]) {
          flag = true;
          break;
        }
      }
      if (!flag) answer++;
    }
  }

  return answer;
}

let arr = [
  [5, 3, 7, 2, 3],
  [3, 7, 1, 6, 1],
  [7, 2, 5, 3, 4],
  [4, 3, 6, 4, 1],
  [8, 7, 3, 5, 2],
];
console.log(solution(arr));
