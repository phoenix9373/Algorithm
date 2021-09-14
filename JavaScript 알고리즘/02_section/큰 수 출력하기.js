function solution(arr) {
  let answer = [];
  let prev;

  for (const k of arr) {
    if (!prev) {
      answer.push(k);
    } else {
      if (prev < k) answer.push(k);
    }
    prev = k;
  }
  return answer.join(" ");
}

let arr = [7, 3, 9, 5, 6, 12];
console.log(solution(arr));
