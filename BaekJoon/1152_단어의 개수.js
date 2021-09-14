var fs = require("fs");

// 문자 하나만 입력받을 경우
var input = fs.readFileSync("/dev/stdin").toString().trim();

function solution(str) {
  if (str === "") return 0;
  return str.split(" ").length;
}

console.log(solution(input));
