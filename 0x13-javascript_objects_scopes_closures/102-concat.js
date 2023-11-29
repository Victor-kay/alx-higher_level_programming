#!/usr/bin/node

const fs = require('fs');

const [sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv.slice(2);

try {
  fs.writeFileSync(destinationFilePath, fs.readFileSync(sourceFilePath1, 'utf8') + fs.readFileSync(sourceFilePath2, 'utf8'));
  console.log('Files concatenated successfully!');
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
