//Syntax to initialize express in a file
const express = require('express');
const path = require('path');

const app = express();

// setup static folder (public)
// Middleware is a function that runs between the incoming request 
//and the outgoing response.
// This static middleware finds the path of the folder and 
// app.use(express.static(path.join(__dirname, 'public')));

//Pseudo Database
let posts = [
    {id: 1, title: "Post One"},
    {id: 2, title: "Post Two"},
    {id: 3, title: "Post Three"}
]


app.get('/api/posts', (req, res) => {

});

// app.get('/', (req, res) => { 
//     // Sending the HTML file in the public/index.html dir path
//    res.sendFile(path.join(__dirname,  'public', 'index.html'));
// });

// app.get('/about', (req, res) => {
//     res.sendFile(path.join(__dirname,'public', 'about.html'));
// });

app.listen(8000, () => console.log(`Server is running on port 8000`));