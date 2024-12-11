//Module included with node.js
import http, { request } from 'http';
const PORT = 8000;

const server = http.createServer((req, res) => {
    // Method to set Header content type to html
    // Will use HTML tags
    res.writeHead(500, {'Content-Type': 'application/json'});
    // When using express, you don't have implement res.end()
    // Sending information to the client (i.e. browser)
    res.end('<h1>Hello World</h1>');
}); 

server.listen(PORT,() => {
    console.log(`Server on port port ${PORT}`);
});

