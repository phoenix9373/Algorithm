console.time("for");

const MAX_LENGTH = 30000;
const MAX = 1000000000;

const bigA = Array.from({ length: MAX_LENGTH }, (_) => getRandomInt(1, MAX));
const bigB = Array.from({ length: MAX_LENGTH }, (_) => getRandomInt(1, MAX));

function quickSort(arr) {
  const L = arr.length;

  if (L < 2) return arr;

  let l = 0;
  let m = Math.floor(L / 2);
  let r = L - 1;

  const pivot = arr[m];

  while (l < r) {
    while (arr[l] < pivot) l++;

    while (arr[r] > pivot) r--;

    if (l <= r) {
      let swap = arr[l];
      arr[l] = arr[r];
      arr[r] = swap;
      l++;
      r--;
    }
  }

  return quickSort(arr.slice(0, r + 1)).concat(quickSort(arr.slice(r + 1)));
}

function solution(arr1, arr2) {
  arr1 = quickSort(arr1);
  arr2 = quickSort(arr2);

  const answer = [];

  while ()
}

let a = [1, 3, 9, 5, 2];
let b = [3, 2, 5, 7, 8];

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

console.log(solution(a, b));
console.timeEnd("for");
