let firstName = 'Steven';
let firstName2 = 'Shane';

const christmas_2024 = '12.24.2024';
// console.log(christmas_2024);

// Primitive Data

let favouriteFruit = 'strawberries';
let favouriteIceCream = 'chocolate';
let favouriteProgrammingLanguage = 'Javascript';

// Reference Data

let numberOfDonuts = 12;
let pi = 3.14;
let veryLargeNumber = 13128910248109n;

let lovesCoding = true;

// null to clear the value of data
favouriteFruit = null;

// Objects
let course = {
    name: 'Javascript for Beginners',
    hours: 3
};
//console.log(course.name);

let property = 'hours';
//console.log(course['hours']);

// Arrays
let productColors = ['blue','green', 'yellow', 'red'];

//console.log(productColors);
//console.log(productColors[0]);

// Functions
function sayHi(name) {
    name = 'Shane';
    console.log(`Hi! ${name}`);
}

sayHi();

function multiply(num1, num2) {
    return num1 * num2;
}

console.log(multiply (2,2));