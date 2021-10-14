console.time("for");

const MAX_LENGTH = 30000;
const MAX = 1000000000;

const bigA = Array.from({ length: MAX_LENGTH }, (_) => getRandomInt(1, MAX));
const bigB = Array.from({ length: MAX_LENGTH }, (_) => getRandomInt(1, MAX));

function quickSort(arr) {
  const L = arr.length;

  if (L < 2) return arr;

  const left = [];
  const right = [];
  const pivot = [arr[0]];

  for (let i = 1; i < L; i++) {
    if (arr[i] < pivot[0]) left.push(arr[i]);
    if (arr[i] > pivot[0]) right.push(arr[i]);
    if (arr[i] === pivot[0]) pivot.push(arr[i]);
  }

  return quickSort(left).concat(pivot, quickSort(right));
}

function solution(firstArray, secondArray) {
  firstArray = quickSort(firstArray);
  secondArray = quickSort(secondArray);

  const answer = [];

  let i = 0;
  let j = 0;

  while (i < firstArray.length || j < secondArray.length) {
    if (i >= firstArray.length) {
      while (j < secondArray.length) {
        answer.push(secondArray[j]);
        j++;
      }
      break;
    }

    if (j >= secondArray.length) {
      while (i < firstArray.length) {
        answer.push(firstArray[i]);
        i++;
      }
      break;
    }

    if (firstArray[i] >= secondArray[j]) {
      answer.push(secondArray[j]);
      j++;
    }

    if (secondArray[j] > firstArray[i]) {
      answer.push(firstArray[i]);
      i++;
    }
  }

  return answer;
}

let a = [1, 3, 9, 5, 2];
let b = [3, 2, 5, 7, 8];

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

// check
const mergedArray = quickSort(bigA.concat(bigB));
const resultArray = solution(bigA, bigB);

let count = 0;
for (let i = 0; i < mergedArray.length; i++) {
  if (mergedArray[i] !== resultArray[i]) {
    count++;
  }
}

console.log("wrong case count: ", count);
console.timeEnd("for");
