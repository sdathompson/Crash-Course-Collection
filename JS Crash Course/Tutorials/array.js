//Adding Elements
const numbers = [5, 4, 3, 2, 1];

//adds elements to the end
numbers.push(7, 8, 9); // output = [5, 4, 3, 2, 1, 7, 8, 9]

//adds elements to the start
numbers.unshift(25, 24); //output = [25, 24, 5, 4, 3, 2, 1, 7, 8, 9]

// first value asks where you want to add values, 
// second value asks how many values you want to delete, 
// rest of the values pertain to what you want to add to the array

numbers.splice(1, 0, 25, 24); //output = [5, 25, 24, 4, 3, 2, 1]

//Finding Elements (Primitives)

const indexofThree = numbers.indexOf(3); // output = return the index of the number 3 in the array. if it doesn't exist, return -1
const lastIndexOfThree = numbers.lastIndexOf(3); // output = the last index value of 3 in the array.
const indexOFTen = numbers.lastIndexOf(10); // output = If it doesn't exist, -1

//Finding Elements (References)

const employees = [
    {
        id: 1,
        name: 'Jim'
    },
    {
        id: 2,
        name: 'Michael Scott'
    },
    {
        id: 3,
        name: 'Pam'
    },
];

// To find a certain object, use the .find() method to callback a function.
// const employee = employees.find(function(e) {
//     return e.name === 'Jim' // output = {id: 1, name: 'Jim'}
// });

// const employeeIdx =  employees.findIndex(function(e) {
//     return e.name === 'Jim' // output = 0 (the index of the Jim object)
// });

// Arrow Functions

const add = (num1, num2) => num1 + num2;

const employee = employees.find((e) => e.name === 'Jim');
const employeeIdx = employees.findIndex((e) => e.name === 'Pam');

//Removing Elements

const lastElement = numbers.pop(); //output = remove the last element
const firstElement = numbers.shift(); //output = remove the first element
const middleElement = numbers.splice(3, 1); //output = remove elements in the specified area, extra parameters after the second will replace those numbers.

// Emptying an Array
let arrayNumber = [5, 4, 3, 2, 1];

//While Loop Method
// while (arrayNumber.length > 0)
//     arrayNumber.pop();

//Assignment Method
//array.length = 0;

//Splice Method
//const deletedNumbers = numbers.splice(0, numbers.length);

//Assigning the current array to a new array
arrayNumber = [6, 7, 8, 9, 0];

// Combining and Slicing Arrays
const exampleNumbersA = [1, 2, 3, 4, 5];
const exampleNumbersB = [6, 7, 8, 9, 0];

const combinedArray = exampleNumbersA.concat(exampleNumbersB);

const firstSlice = combinedArray.slice(0, 4);

// Spread Operator
let combined = [...exampleNumbersA, 9, ...exampleNumbersB, 10];

let a = [1, 2];
let b = [...a];

//Iterating an Array
for (let number of combined) {
    // Iterate through the array
}

combined.forEach((number) =>{
    //Iterate through the array
});

//Joining Arrays
const numbersJoin = [1, 2, 3, 4, 5];
const joinedNumbers = numbersJoin.join(', ');
//output = 1, 2, 3, 4, 5

const action = 'I went to the store';
const splitString = action.split(' ');
//output = [I, went, to, the, store] (splits at the empty value)
const urlSlug = action.join('-');
//output = I-went-to-the-store

//Sorting Arrays
let characters = ['c','d', 'b', 'a'];
characters.sort(); //output = ['a', 'b', 'c', 'd']
characters.reverse(); //output = ['d', 'c', 'b', 'a']

let newEmployees = [
    { id: 1, name: 'Jen'},
    { id: 2, name: 'Rob'},
    { id: 3, name: 'Ana'},
    { id: 4, name: 'Boris'},
];

//Alphabetical Sort Based off of the name property
employee.sort((a, b) => {
    // Computers use ASCII values to sort. Uppercase letters have lower ASCII values than lowercase letters
    const lowercaseA = a.name.toLowerCase();
    const lowercaseB = b.name.toLowerCase();

    // Return negative means that object A comes before object B
    if (lowercaseA < lowercaseB) return -1;
    if (lowercaseA > lowercaseB) return 1;
    return 0;
});

//Testing the Elements of an Array
const evenNumbers = [2, 4, 6, 8, 10];

const areAllEven = evenNumbers.every(number => number % 2 === 0);
// output = true

const areSomeEven = evenNumbers.some(number => number % 2 === 0);
//output = true, would be true even if 2 was the only even number

// Filtering an Array
const filterArray = [1, 2, 3, 4, 5, 6];
const evenFNumbers = numbers.filter(number => number % 2 === 0);
//output = if a number in filterArray is even, it gets added to evenFNumbers

const fEmployees = [
    {id: 1, name:'Alice', role: 'Developer'},
    {id: 2, name:'Bob', role: 'Designer'},
    {id: 3, name:'Charlie', role: 'Developer'},
    {id: 4, name:'Danielle', role: 'Manager'},
];

const developers = fEmployees.filter(empIdx => empIdx.role === 'Developer');
// if the role is 'Developer', add it to the developers array

// Mapping an Array
const mNumbers = [2, 4, 6, 8, 10];
const squaredNumbers = numbers.map(num => num * num);
//output = 4, 16, 36, 64, 100

const uCharacters = ['a', 'b', 'c', 'd', 'e', 'f'];
const upperCaseCharacters = uCharacters.map(character => character.toUpperCase());
//output = ['A','B','C','D','E','F']

const lEmployees = [
    { id: 1, name: 'Alice', email: 'AliCe@gmail.com'},
    { id: 2, name: 'Steven', email: 'SteVen@gmail.com'},
    { id: 3, name: 'Shane', email: 'sDA.ThOmPsOn@hotmail.com'},
];

// Must use a spread operator to copy the properties
const updatedEmployees = lEmployees.map(employee => ({
    // Once you copied the object, you can set new properties
    ...employee,
    email: employee.email.toLowerCase()
}));

// Reducing an Array

const rNumbers = [1, 10, 5, 14];
// let sum = 0;

// for (const num of rNumbers) {
//     sum += num;
// }

// const sum = numbers.reduce((accumlator, currentValue) => {
//     return accumlator + currentValue;
// // 0 is the initial value passed into the reduce method
// }, 0);

const sum = numbers.reduce((accumlator, currentValue) => accumlator + currentValue);
//output adds all the elements in the array together