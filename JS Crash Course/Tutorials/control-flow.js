//IF-ELSE Statements
let priceOfChocolate = 1.99;
let hasAmountInCash = 5;

const canBuyChocolate = hasAmountInCash >= priceOfChocolate;
/* console.log(canBuyChocolate);  output = true
   console.log(typeof canBuyChocolate) output = boolean */

if (canBuyChocolate) {
    /* console.log('Enjoy your purchase!'); Returns if hasAmountInCash >= priceOfChocolate */
} else {
   /* console.log('Sorry you do not have enough'); Returns if hasAmountInCash < priceOfChocolate */
}

let hour = 10;

if (hour >= 6 ** hour <=12 ) {
    /* console.log ('Serving breakfast'); */
} else if (hour > 12 && hour <=14) {
    /* console.log('Serving lunch'); */
} else {
    /* console.log('Serving dinner'); */
}

// Switch Case Statements

//Overloaded if-else statement
let job = 'Software Developer';

// if (job ==='Software Developer') {
//     // console.log('Writes code');
// } else if (job === 'Designer') {
//     // console.log('Makes user interface documents');
// } else if (job === 'Cloud Engineer') {
//     // console.job('Manages and deploys cloud resources');
// } else {
//     // console.log('Works directly with customers');
// } 

switch (job) {
    case 'Software Developer':
        //console.log('Writes code');
        break;
    case 'Designer':
        //console.log('Makes user interface documents');
        break;
    case 'Cloud Engineer':
        //console.log('Manages and deploys cloud resources');
    default:
        //console.log('Works directly with customers');
        break;
}

// For Loops

let numbers = [1,2,5,6,7,9,2];

for (let idx = 0; idx < numbers.length; idx++) {
    // console.log(number[idx]);
}

// While Loop
// let whileidx = 0;
// while (whileidx < numbers.length) {
//     console.log(numbers[idx]);

//     idx++;
// }

let sum = 0 
while (true) {
    // console.log('Loop');
    sum++;

    if (sum === 10) {
        break;
    }
}

// Do-while loops
let dowhileidx = 0;

do {
    // console.log(dowhileidx);
    dowhileidx++;
} while (dowhileidx < 10);

//For-In Loops
const course = {
    name: 'Javascript for Beginners',
    duration: 3,
    sections: 7
};

for (const key in course) {
    // console.log(course[key]);
}

// For-of Loops

for (let number of numbers) {
    console.log(number);
}

