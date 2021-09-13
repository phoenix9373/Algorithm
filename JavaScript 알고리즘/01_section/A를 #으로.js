function solution(s) {
  let answer = Array.from(s).map((c) => (c === "A" ? "#" : c));

  return answer.join("");
}

function solution2(s) {
  let answer = s.replace(/A/g, "#");
  return answer;
}

let str = "BANANA";
console.log(solution2(str));
