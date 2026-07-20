#!/usr/bin/node

const args1 = Number(process.argv[2])
const args2 = Number(process.argv[3])

function add(a, b){
    if(Number.isInteger(a) && Number.isInteger(b)){
        console.log(a + b)
    }
    else{
        console.log("NaN")
    }


}
add(args1, args2)