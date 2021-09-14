const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let count;
let idx = 0;

rl.on("line", function (line) {
  if (!count) {
    count = parseInt(line.toString().trim());
  } else {
    input.push(line);
    idx++;
  }

  if (idx === count) rl.close();
}).on("close", function () {
  solution(input);
  process.exit();
});

function solution(input) {
  input = input.map((s) => s.split(" ")).map((k) => [parseInt(k[0]), k[1]]);
  const res = input.map((s) => {
    let value = "";
    for (const c of s[1]) {
      value += c.repeat(s[0]);
    }
    return value;
  });

  for (const r of res) console.log(r);
}
