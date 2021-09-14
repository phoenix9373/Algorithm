// charCodeAt : 문자열을 아스키코드로 변환
// fromCharCode : 아스키코드를 문자열로 변환
// A-Z : 65-90
// a-z : 97-122

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

console.log(input.charCodeAt(0));
