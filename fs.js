var fs = require("fs");

// 문자 하나만 입력받을 경우
var input = fs.readFileSync("/dev/stdin").toString();

// input[0], input[1] 배열에서 꺼내쓰면 된다.
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

// 줄바꿈으로 구분
var input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 만약 인풋값이 숫자라면
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(function (a) {
    return +a;
  });
