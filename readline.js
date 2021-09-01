const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = 0;

rl.on("line", function (line) {
  count++;

  console.log(line);

  if (count === 3) rl.close();
}).on("close", function () {
  process.exit();
});
