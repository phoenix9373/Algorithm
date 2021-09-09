const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let line;

rl.on("line", function (line) {
  line = line.split(" ");
  rl.close();
}).on("close", function () {
  process.exit();
});
