const loadJoke = async () => {
    try{
        const chuckNorrisFetch = await ('https://api.chucknorris.io/jokes/random', {
            headers: {
                Accept: "application/json"
            }
        });

        const jokeData = await chuckNorrisFetch.json();
        document.getElementById('loadingJoke').innerHTML = jokeData.value;
    } 
    catch(error) {
        console.log(error);
    }
}

