// Object Literal
const dog = {
    name: 'Max',
    breed: 'Dachshund',
    age: 5,
    weightInPounds: 12, 

    //two ways of calling functions in objects
    eat: function () {
        // console.log('Chomp!');
    },
    bark () {
        // console.log('Woof!');
    }
}

//Factory Functions
function getDog(name, breed, age, weightInPounds) {
    return {
        name,
        breed,
        age,
        weightInPounds,
        eat(munch) {
            // console.log('munch');
        },
        bark(sound) {             
           // console.log('sound');
        }
    }
}

const anotherDog = getDog('Marley', 'Chocolate', 3, 60);
// console.log(anotherDog);

// Constructor Functions
function Dog(name, breed, age, weightInPounds) {
    // this = {};
    //Add properties to this
    this.name = name;
    this.breed = breed;
    this.age = age;
    this.weightInPounds = weightInPounds;

    this.eat = function() {
        // console.log(this.name + ': Chomp!' );
    }

    this.bark = function() {
       // console.log(this.name + ': Woof!');
    }

    // return this;
}

const yetAnotherDog = new Dog('Marley', 'Lab', 3, 60);

// Objects are Dynamic
const person = {
    name: 'Shane'
};

console.log(person); // output = name: Shane
person.favoriteFood = 'sushi';
console.log(person); //output = name: Shane, favouriteFood: sushi

delete person.favoriteFood;
console.log(person); //output = name: Shane

person.eat = () => {
    console.log('start eating!');
}

person.eat(); // output = start eating!

//Constructor Property
// let newObj = {}; these two lines do the same thing
// let newObj = new Object(); the one above is the shortform

new String(); // 'Shane'
new Boolean(); // true, false
new Number(); // 1, 2, 3

//Enumerating Properties of an Object
let numbers = [1,2,3,4,5];

for (const elements of numbers) {
    console.log(elements);
}

//Enumerating Properties of an Object
const diggidtyDog = {
    name: 'Max',
    age: 5,
    eyeColor: 'blue'
};

//tester for-in loop
// for (const key in diggidtyDog) {
//     console.log(diggidtyDog[key]);
// }   // output = [name, age, eyeColor] 

const keys = Object.keys(diggidtyDog); //output = ['name', 'age', 'eyeColor']

const values = Object.values(diggidtyDog); //output = ['Max', 5, 'blue']

const entries = Object.entries(diggidtyDog); // nested array output = [ ['name', 'Max'] ['age', 5], ['eyeColor', 'blue'] ]

// for (const key of Object.keys(diggidtyDog)) {
//     console.log(key);
// } //array output = name age eyeColor 

// Cloning an Object
let a = {value: 10};

// This clones the contents of object a to the empty object b
// Object.assign(b,a);
let b = { ...a};

b.value = 20;

//Built-in Math Functions
const getRandomInt = (min,max) => {
	return Math.round(Math.random() * (max-min) + min);
}

console.log(getRandomInt(1,100));

// String Methods

let sentence = "A new sentence.";

const doesIncludeNew = sentence.includes('new'); //output = true
const sentenceIndex = sentence[3]; //output = e 
const startswithA = sentence.startsWith('A'); //output = true
const endswithA = sentence.endsWith('A'); //output = false

let updatedSentence = sentence.replace('new', 'short'); //output = A short sentence

trimmedSentence = sentence.trim(); //output = removes the spaces from the beginning and the end

const wordsInSentence = sentence.split(' '); //wherever the method encounter this character, a space, it will split it into the array

let email = 'TesTEmail@gmail.com';

let lowerCaseEmail = email.toLowerCase(); //makes everything typed register as lower-case.
let upperCaseEmail = email.toUpperCase(); //makes everything typed registed as upper-case.

//Template Literal
let firstName = 'Shane';
let lastName = 'Thomspon';
let fullName = `${firstName} ${lastName}`; //template lit
