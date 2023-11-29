#!/usr/bin/node

const arg = process.argv[2]; // Extract the first command line argument

if (arg === undefined) {
  console.log("No argument");
} else {
  console.log(arg);
}
