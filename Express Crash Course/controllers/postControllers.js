// Get all posts
// route GET /api/posts

let posts = [
    {id: 1, title: "Post One"},
    {id: 2, title: "Post Two"},
    {id: 3, title: "Post Three"}
];


export const getPosts = (req, res, next) => {
    console.log(req.query);
    const limit = parseInt(req.query);    
// If a limit that is a number is given, it will show all posts up to the limit
// else it will return all posts
    if (!isNaN(limit) && limit > 0) {        
        return res.status(200).json(posts.slice(0, limit));        
    }

    res.status(200).json(posts);
    
};

// Get a single post
// route GET /api/posts/:id

export const getPost = (req, res, next) => {
    //parseInt to go from a string to a number
    const id = parseInt(req.params.id);
    //filter the current ID into the URL
    const post = posts.find((post) => post.id === id);

    if (!post) {
        const error = new Error(`A post with the id of ${id} was not found`);
        error.status = 404;
        return next(error);
    }      
    
    res.status(200).json(post);
    
};

// Create a post
// route POST api/posts/

export const createPost = (req, res, next) => {
    // Create an object to be pushed onto the array
    const newPost = {
        id: posts.length + 1,
        title: req.body.title
    };

    // Null case
    if (!newPost.title) {
        const error = new Error ('Please include a title');
        error.status = 400;
        return next(error);
        
    }

    // 
    posts.push(newPost);
    res.status(201).json(posts);
};


// Update post
// route PUT api/posts/:id

export const updatePost = (req, res, next) => {
    const id = parseInt(req.params.id);
    const post = posts.find((post) => post.id === id);

    if (!post) {
        const error = new Error (`A post with the id of ${id} was not found`);
        error.status = 404;
        return next(error);
    }
    post.title = req.body.title;
    res.status(200).json(posts);
    
    
};

// Delete post
// route DELETE api/posts/:id

export const deletePost = (req, res, next) => {
    const id = parseInt(req.params.id);
    const post = posts.find((post) => post.id === id);

    if (!post) {
        const error = new Error (`A post with the id of ${id} was not found`);
        error.status = 404;
        return next(error);
    }
    post.title = req.body.title;
    res.status(200).json(posts);
    
    
};