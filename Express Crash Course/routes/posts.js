import express from 'express';
import { createPost, deletePost, getPost, getPosts, updatePost } from '../controllers/postControllers.js';
const router = express.Router();

//Pseudo Database
let posts = [
    {id: 1, title: "Post One"},
    {id: 2, title: "Post Two"},
    {id: 3, title: "Post Three"}
];


//Res.json passes a JS array of objects
// Get all posts
router.get('/', getPosts);

// Get a single post (for dynamic branches use '/:attribute' syntax)
router.get('/:id', getPost);

// Create new post
router.post('/', createPost);

//Update post
router.put('/:id', updatePost);

//Delete Post
router.delete('/:id', deletePost);

export default router;