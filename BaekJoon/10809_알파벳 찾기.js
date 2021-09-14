const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;

rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  console.log(solution(input));
  process.exit();
});

function solution(input) {
  const alpabet = Array.from({ length: 123 - 97 }, (_, i) =>
    String.fromCharCode(i + 97)
  );

  const res = [];
  for (const char of alpabet) {
    res.push(input.indexOf(char));
  }

  return res.join(" ");
}
