function solution(s) {
  let answer = 0;

  const stack = [];
  let prev = "";

  for (const c of s) {
    if (c === "(") {
      stack.push(c);
    } else {
      if (prev === "(") {
        stack.pop();
        stack.push("1");
      } else {
        stack.push(c);
      }
    }

    prev = c;
  }

  let numbers = [];

  for (const c of stack) {
    if (c === "1") {
      numbers = numbers.map((v) => v + 1);
    }

    if (c === "(") {
      numbers.push(0);
    }
    if (c === ")") {
      answer += numbers.pop() + 1;
    }
  }

  return answer;
}

let a = "()(((()())(())()))(())";
let b = "(((()(()()))(())()))(()())";
console.log(solution(b));
