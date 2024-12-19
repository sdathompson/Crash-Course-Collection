const express = require('express');
const router = express.Router();

//Pseudo Database
let posts = [
    {id: 1, title: "Post One"},
    {id: 2, title: "Post Two"},
    {id: 3, title: "Post Three"}
];

//Res.json passes a JS array of objects
// Get all posts
app.get('/api/posts', (req, res) => {
    console.log(req.query);
    const limit = parseInt(req.query);    
// If a limit that is a number is given, it will show all posts up to the limit
// else it will return all posts
    if (!isNaN(limit) && limit > 0) {
        return res.status(200).json(posts.slice(0, limit));        
    }

    res.status(200).json(posts);
    
});

// Get a single post (for dynamic branches use '/:attribute' syntax)
app.get('/api/posts/:id', (req, res) => {
    //parseInt to go from a string to a number
    const id = parseInt(req.params.id);
    //filter the current ID into the URL
    const post = posts.find((post) => post.id === id);

    if (!post) {
        return res.status(404).json({msg: `A post with the id of ${id} was not found.`});
    }         
    
    res.status(200).json(post);
    
});