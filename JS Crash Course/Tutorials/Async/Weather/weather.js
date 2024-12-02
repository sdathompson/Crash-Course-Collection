// Weather API key = 3d195e077f02252764df48261c7abf31

const date = document.getElementById('date');
const city = document.getElementById('city');
const temp = document.getElementById('temp');
const tempImg = document.getElementById('tempImg');
const description = document.getElementById('description');
const tempMax = document.getElementById('tempMax');
const tempMin = document.getElementById('tempMin');

// Create an array that has all the possible dates of the year
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

//Common Syntax to grab the Date Object in JS
let dateObj = new Date();

//Target the date Object and getting the months, days, and years
let month = months[dateObj.getUTCMonth()];
// For EST (UTC + 1 timezone)
let day = dateObj.getUTCDay() + 1;
let year = dateObj.getUTCFullYear();

date.innerHTML = `${month} ${day}, ${year}`;

const app = document.getElementById('app');

const getWeather = async () => {
    try {
        // the city will get set to the value put into the search bar
        const cityName = document.getElementById('searchBarInput').value;
        // Fetch API
        const weatherDataFetch = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=3d195e077f02252764df48261c7abf31&units=metric`,
           { headers: {
                Accept: "application/json"
            }
        });

        const weatherData = await weatherDataFetch.json();
        console.log(weatherData);
     
        city.innerHTML = `${weatherData.name}`;
         
        description.innerHTML = `${weatherData.weather[0].main}`;
        // Img tag in backticks grabs the weather array object attribute of icon. Size property before calling the .png
        tempImg.innerHTML = `<img src="http://openweathermap.org/img/wn/${weatherData.weather[0].icon}.png" />`;
        // h2 tag in backticks grabs in temp in the main object. Round the double.
        temp.innerHTML = `<h2>${Math.round(weatherData.main.temp)}°C</h2>`;
        tempMax.innerHTML = `<h5>${Math.round(weatherData.main.temp_max)}°C </h5>`;
        tempMin.innerHTML = `<h5>${Math.round(weatherData.main.temp_min)}°C </h5>`;

    } catch(error) {
        console.log(error)
    }
}


