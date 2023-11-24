#!/usr/bin/node

function factorial(n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }

  if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive case
  }
}

const arg = Number(process.argv[2]);
const result = factorial(arg);

console.log(result);
