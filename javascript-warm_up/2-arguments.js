#!/usr/bin/node

const char = process.argv[2]

if (!char) {
  console.error('No argument')
}
else if(!process.argv[3]){
  console.log("Argument found")
}
else {
  console.log('Arguments found')
}
