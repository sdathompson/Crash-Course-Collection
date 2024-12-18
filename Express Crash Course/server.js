//Syntax to initialize express in a file
const express = require('express');
const path = require('path');
const port = process.env.PORT || 8000;
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
];

//Res.json passes a JS array of objects
// Get all post
app.get('/api/posts', (req, res) => {
    res.json(posts);
});

// Get a single post (for dynamic branches use '/:attribute' syntax)
app.get('/api/posts/:id', (req, res) => {
    //parseInt to go from a string to a number
    const id = parseInt(req.params.id);
    //filter the current ID into the URL
    res.json(posts.filter((post) => post.id === id));
});
// For titles
app.get('/api/posts/:title', (req, res) => {
    //parseInt to go from a string to a number
    console.log(req.params.title);
    //filter the current ID into the URL
    res.json(posts.filter((post) => post.title === title));
});

// app.get('/', (req, res) => { 
//     // Sending the HTML file in the public/index.html dir path
//    res.sendFile(path.join(__dirname,  'public', 'index.html'));
// });

// app.get('/about', (req, res) => {
//     res.sendFile(path.join(__dirname,'public', 'about.html'));
// });

app.listen(port, () => console.log(`Server is running on port ${port}`));