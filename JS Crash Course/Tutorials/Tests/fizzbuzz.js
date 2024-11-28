/* Implement a function t accept a number. 
Then return "FizzBuzz" if divisible by 3 and 5.
Or return "Fizz" if only divisible by 3.
Or return "Buzz" if only divisible by 5.
Or return the original number if not divisible by 3 or 5. */
// Works just use if statements instead
function fizzBuzz(num){
    if (num % 3 === 0 && num % 5 === 0){
        return "FizzBuzz";
    } else if (num % 3 === 0) {
        return "Fizz";
    } else if (num % 5 === 0) {
        return "Buzz";
    } else {
        return num;
    }
}

for (let fidx = 0; fidx < 30; fidx++) {
   console.log(fizzBuzz(fidx));
}