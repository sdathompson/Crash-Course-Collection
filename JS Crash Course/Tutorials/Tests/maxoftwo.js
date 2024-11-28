// Implement a function to accept two numbers and return the maximum number

function twomax(num1,num2){

    if (num1 !== null && num2 !== null){
        if (num1 > num2){
            return num1;
        } else if (num1 < num2){
            return num2;
        } else {
            console.log("The numbers are equal");
        }
    }

}

console.log(twomax(2,1));
console.log(twomax(1, 2));
console.log(twomax(1,1));
console.log(twomax("Bob","Sarah"));