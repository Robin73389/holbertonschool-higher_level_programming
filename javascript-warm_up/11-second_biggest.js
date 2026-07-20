#!/usr/bin/node

const args = (process.argv.slice(2).map(Number))

let first = args[0]
let res = null;

if(args.length === 0){
    console.log(0)
}
if(args.length === 1){
    console.log(0)
}

else{

    args.sort((a, b) => b - a)

    let first = args[0]
    
    for (let i = 1; i < args.length; i++){
        if (args[i] < first){
            res = args[i];
            break;
        }
    }
    console.log(res)
}
