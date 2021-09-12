function solution(arr) {
  let answer = arr;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (i === j) continue;
      let tmp = arr.filter((_, idx) => idx !== i && idx !== j);
      let sum = tmp.reduce((acc, cur) => acc + cur, 0);
      if (sum === 100) answer = tmp;
    }
  }
  return answer;
}

let arr = [20, 7, 23, 19, 10, 15, 25, 8, 13];
console.log(solution(arr));
