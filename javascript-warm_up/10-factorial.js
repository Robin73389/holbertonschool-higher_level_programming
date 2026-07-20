#!/usr/bin/node

const args = Number(process.argv[2])

function fact(n){
    if (n === 0 || n === 1){
        return 1;
    }
    return n * fact(n - 1)
}
console.log(fact(args))