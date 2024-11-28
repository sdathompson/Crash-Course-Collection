/*, -, +, *, /, % */

let a = 10;
a++; //increment the value
++a; //increment the value and return that updated value
a--; // decrement the value
--a; //decrement the value and return the updated value


// Comparison Operators
let num1 = 14;
let num2 = 10;

const isNum1Greater = num1 > num2;
/* console.log(isNum1Greater); output = true */

const isNum1GreaterOrEqualTo = num1 >= num2;
/* console.log(isNum1GreaterOrEqualTo); output = true */

const isNum1Less = num1 < num2;
/* console.log(isNum1Less); output = false */

const isNum1LessOrEqual = num1 <= num2;
/* console.log(isNum1LessOrEqual); output = false */


//Equality Operators
let a1 = 2;
let b1 = '2';

/* console.log(a == b); output = true because it uses loose equality */
/* console.log(a === b); output = false because it uses strict equality */

//Ternany Operator
let age = 16;
const canDrive = age >= 16 ? true : false;
// ^ same as writing if (age >= 16) {
//     return true;
//     }else{
//     return false;
//     }

let points = 110;
const customerType = points > 100 ? "gold" : "silver";

// Logical Operation
// OR operator
/* console.log(true || true); output = true */
/* console.log(false || true); output = true */
/* console.log(true || false); output = true */
/* console.log(false || false); output = false */

let hasReservation = true;
let acceptingWalkIns = false;

const hasAccessToTable = hasReservation || acceptingWalkIns;
/* console.log(hasAccessToTable); output = true */

// AND operator
/* console.log(true && true); output = true */
/* console.log(false && true); output = false */
/* console.log(true && false); output = false */
/* console.log(false && false); output = false */

let a2 = true, b2 = true, c2 = true, d2 = true;
/* console.log((a && b) || (c && d)); output = true, order of operations */

// NOT Operator
let isClosedOnSunday = true;
const isRestaurantOpen = !isClosedOnSunday;
/* console.log(isRestaurantOpen); output = false */

// NULL Operator
let a3 = null;
const result = a ?? false; //shorthand of (a3 !== null && a3 !== undefined) ? a3 : false;

/* console.log(result); //output = true */


// Logical Operators with Non-boolean operands
let userChosenColor = 'blue';
let defaultColor = 'green';

const currentWebsiteColor = userChosenColor || defaultColor;
/* console.log(currentWebsiteColor); output = blue, evaluates from left-to-right and picks the first truthy expression */

// Operator Precedence
let n = 5 + (5 * 4);
/* console.log(n); output = 25 */
