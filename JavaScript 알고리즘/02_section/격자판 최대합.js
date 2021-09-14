function solution(arr) {
  let answer = Number.MIN_SAFE_INTEGER;
  let Ldig = 0;
  let Rdig = 0;

  for (let i = 0; i < arr.length; i++) {
    let row = 0;
    let col = 0;

    for (let j = 0; j < arr.length; j++) {
      row += arr[i][j];
      col += arr[j][i];
      if (i === j) Ldig += arr[i][j];
      if (i + j + 1 === arr.length) Rdig += arr[i][j];
    }

    if (answer < row) answer = row;
    if (answer < col) answer = col;
  }

  if (answer < Ldig) answer = Ldig;
  if (answer < Rdig) answer = Rdig;

  return answer;
}

let arr = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
];
console.log(solution(arr));
