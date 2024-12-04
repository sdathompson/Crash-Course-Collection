function generateRandomNumber () {
    return Math.floor(Math.random() * 100) + 1;
}

function celciusToFahrenheit(celcius) {
    return (celcius * 9/5) + 32;
}

//Old syntax: To export multiple functions, use an object
// module.exports = {
//     generateRandomNumber,
//     celciusToFahrenheit,
// }