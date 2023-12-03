'use strict'
const fs = require('fs')

function Main(input) {
    input = input.split(' ').map(x => parseInt(x, 10))
    const a = input[0]
    const b = input[1]
    const c = input[2]
    const abc = [a, b, c]
    const abc5 = abc.filter(x => x === 5).length
    const abc7 = abc.filter(x => x === 7).length
    if (abc5 === 2 && abc7 === 1) {
        console.log('YES')
    } else {
        console.log('NO')
    }
    process.exit(0)
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (answer) => {
    Main(answer);
});
