const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let count = 0;
let repeat = 2;

rl.on("line", function (line) {
  input.push(line);
  count++;
  if (count === repeat) rl.close();
}).on("close", function () {
  console.log(solution(input));
  process.exit();
});

function solution(input) {
  const values = input.map((v) => v.trim());
  let res = 0;

  for (const v of values[1]) {
    res += parseInt(v);
  }

  return res;
}
