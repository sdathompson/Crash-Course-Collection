//Syntax to initialize express in a file
const express = require('express');

const app = express();

app.get('/', (req, res) => { 
    // Don't have to define the content type. Automatically update to the desired content
    res.send({message: 'Hello World'});
    res.end();
});

app.get('/about', (req, res) => {
    res.send('About');
});

app.listen(8000, () => console.log(`Server is running on port 8000`));