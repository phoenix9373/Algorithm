function solution(need, plan) {
  const arr = [];

  for (const c of plan) {
    if (need.includes(c)) arr.push(c);
  }

  if (arr.join("") === need) return "YES";
  else return "NO";
}

let a = "CBA";
let b = "CBDAGE";
console.log(solution(a, b));
