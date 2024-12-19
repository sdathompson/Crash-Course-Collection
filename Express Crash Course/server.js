//Syntax to initialize express in a file
import express from 'express';
import path from 'path';
import posts from './routes/posts.js';
import logger from './middleware/logger.js';
import error from './middleware/error.js';
const port = process.env.PORT || 8000;

const app = express();

//Body parser middleware
//To parse raw JSON data
app.use(express.json());

//To parse URL encoded data
app.use(express.urlencoded({ extended: false }));

//Logger middleware
app.use(logger);

//Error handler
app.use(errorHandler);

// setup static folder (public)
// Middleware is a function that runs between the incoming request 
//and the outgoing response.
// This static middleware finds the path of the folder and 
// app.use(express.static(path.join(__dirname, 'public')));

//Routes
//In the .use setup the file directory and delete it from the route file
app.use('/api/posts', posts);

app.listen(port, () => console.log(`Server is running on port ${port}`));