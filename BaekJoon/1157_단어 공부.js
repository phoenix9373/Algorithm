const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

function solution(str) {
  let ans;
  let max = Number.MIN_SAFE_INTEGER;
  const store = {};

  // 65-90 / 97-122
  for (const c of str) {
    const code = c.charCodeAt(0);
    if (code < 91 && code >= 65) {
      store[code] = store[code] ? store[code] + 1 : 1;
      if (max < store[code]) max = store[code];
    } else {
      store[code - 32] = store[code - 32] ? store[code - 32] + 1 : 1;
      if (max < store[code - 32]) max = store[code - 32];
    }
  }

  let cnt = 0;
  for (const [k, v] of Object.entries(store)) {
    if (v === max) {
      cnt++;
      ans = String.fromCharCode(k);
    }
    if (cnt === 2) return "?";
  }

  return ans;
}

console.log(solution(input));
