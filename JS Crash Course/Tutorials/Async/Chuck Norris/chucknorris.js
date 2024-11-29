const loadJoke = async () => {
   // Call the try-catch method and add the header to accept the .json
    try{
        //Await the fetch of the API
        const chuckNorrisFetch = await fetch('https://api.chucknorris.io/jokes/random', {
            headers: {
                // Headers section accept the .JSON app data
                Accept: "application/json"
            }
        });

        // Fetch the .JSON from the data provided
        const jokeData = await chuckNorrisFetch.json();
        // Get the value from the joke data to display in the HTML
        document.getElementById('loadingJoke').innerHTML = jokeData.value;
    } 
    catch(error) {
        console.log(error);
    }
}

//To get the joke, target the button to load the async function to get a random joke for us
document.getElementById('loadJokeBtn').addEventListener("click", loadJoke);
