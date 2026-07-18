#!/usr/bin/node

const number = new Number(process.argv[2])

const value = parseInt(process.argv[2])

if (isNaN(value)){
    console.log("")
}

if (Number.isInteger(number.valueOf())){
    console.log("My number: " + number)
}
else{
    console.log("Not a number")

}