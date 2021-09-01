// 한 줄만 받는 경우.
var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a + b);

// 여러 줄 받기.
(function () {
  var inputLines = require("fs")
    .readFileSync("/dev/stdin") // 동기적으로 받기.
    .toString()
    .split("\n");
  var meta = inputLines[0].split(" ").map(function (cardNumber) {
    return parseInt(cardNumber); // parseInt로 String => Number
  });
  var cardsLen = meta[0],
    maxSum = meta[1];
  var cards = inputLines[1].split(" ").map(function (cardNumber) {
    return parseInt(cardNumber);
  });

  console.log(solve(cardsLen, maxSum, cards));
})();
