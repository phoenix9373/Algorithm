function solution(m, arr) {
  // N개 중 M개 출력
  // 순서대로 나열

  function permutation(arr, cnt) {
    const results = [];
    if (cnt === 1) return arr.map((value) => [value]);

    arr.forEach((v, i, origin) => {
      const rest = [...origin.slice(0, i), ...origin.slice(i + 1)];
      const permu = permutation(rest, cnt - 1);
      const attached = permu.map((tmp) => [v, ...tmp]);
      results.push(...attached);
    });

    return results;
  }

  return permutation(arr, m);
}

let arr = [3, 6, 9];
console.log(solution(2, arr));
