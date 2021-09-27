function solution(a, b) {
  let answer = [];
  for (let i = 0; i < a.length; i++) {
    let A = a[i];
    let B = b[i];

    if (A === B) {
      answer.push("D");
      continue;
    }

    if (B - (A % 3) === 1) answer.push(" B");
    else answer.push("A");
  }
  return answer;
}

let a = [2, 3, 3, 1, 3];
let b = [1, 1, 2, 2, 3];
console.log(solution(a, b));
