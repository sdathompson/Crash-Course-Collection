// Function Arguments
function multiply(num1,num2) {
    let product = 1;
    // Iterating through the arguments object allow you to add new arguments on the fly
    // in the calling of the function
    for (const num of arguments)
        product *= num;

    return product;
}

multiply(2,2,4); //output = 16 even though there are only two arguments

// The Rest Operator
function multiplyRest(...args) {
    return args.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
}

multiply(1,2,3,4); //output = 24

function multiplyRestB(multiplier, ...numbers) {
    return numbers.map(number => number * multiplier);
}

multiply(2, 1,2,3,4); //first argument is multiplier, rest are the numbers array
// output = [2, 4, 6, 8]

// Default Parameters
function codeDetails(language = 'JavaScript', tool = 'VS Code') {
    //console.log(`Writing code in ${language} using ${tool}`);
}

codeDetails(); //output = Writing code in Javascript using VS Code

// Getters and Setters
const course = {
    name: 'Javascript for Beginners',
    duration: '3 hours',
    get details() {
        // Using the `this` keyword to access key-value pairs in the method
        return `${this.name} is ${this.duration}`
    },
    set details(value) {
        if (typeof value !== 'string') return;

        let parts = value.split(' is ');
        this.name = parts[0];
        this.duration = parts[1];
    }
};

// To catch an error without disrupting the program
try {
    course.details = 42;
} catch (e) {
    console.log(`Caught an error: ${e.message}`);
}