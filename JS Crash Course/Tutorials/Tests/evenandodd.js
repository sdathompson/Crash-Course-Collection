/* Implement two functions. 
For the first function, ha ve it accept an array as a parameter
which contains a list of numbers.
Then console log the even numbers in the array. 
For the second function, have it accept an array and log the odd numbers */

array = [1, 0, 6, 7, 4, 3, 78, 98, 103, 45, 2, 7, 68, 46];

function even(){
    for (let idx = 0; idx < array.length; idx++){
        array[idx] % 2 === 0 ? console.log(array[idx]) : console.log("Not even");       
    }
}

even();

function odd(){
    for (let idx = 0; idx < array.length; idx++){
        array[idx] % 2 !== 0 ? console.log(array[idx]) : console.log("Not odd");
    }
}

odd();