// To import the createServer function
import { createServer } from 'http';
// To import the PORT info from the .env file
const PORT = process.env.PORT;

// Hardcoding data that would most likely come from a database
const users = [
    {id: 1, name: 'John Doe'},
    {id: 2, name: 'Bruce Wayne'},
    {id: 3, name: 'Selina'}
];

// Logger middleware
const logger = ( req, res, next ) => {
    console.log(`${req.method} ${req.url}`);
    // Called to move onto the next part of the middleware function
    next();
};

// JSON middleware
const jsonMiddleware = (req, res, next) => {
    res.setHeader('Content-Type', 'application/json');
    next();
};

// Route Handler for GET /api/users
const getUsersHandler = (req, res) => {
    res.write(JSON.stringify(users));
    res.end();  
};

//Route Handler for GET /api/users/[id number]
const getUserByIdHandler = (req, res) => {
    // Split the request url into an array and grab the 4th elements, which is the ID
    const id = req.url.split('/')[3];
    // Find the user in the array and parse its corresponding ID number
    const user = users.find((user) => user.id === parseInt(id));
    if (user) {            
        res.write(JSON.stringify(user));   
    } else {            
        res.statusCode = 404;
        res.write(JSON.stringify({message: 'User not found'}));
    }
    res.end();
};

//Route Handler for NOT FOUND
const getNotFoundHandler = (req, res) => {
    res.statusCode = 404;
    res.write(JSON.stringify({message: 'Route not found'}));
    res.end();
};

 
const server = createServer((req, res) => {
    logger(req, res, () => {
        jsonMiddleware (req, res, () => {
            if (req.url === '/api/users' && req.method === 'GET') {
                getUsersHandler(req, res);
            } else if (
                req.url.match(/\/api\/users\/[0-9]+/) && 
                req.method === 'GET'
            ) {
                getUserByIdHandler(req, res);
            } else {
                getNotFoundHandler(req, res);
            }
        });
    });

});

server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});