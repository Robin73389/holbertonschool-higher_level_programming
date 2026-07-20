#!/usr/bin/node

const char = process.argv[2]

if (!char) {
  console.error('No argument')
}
else {
  console.log('Arguments found')
}
