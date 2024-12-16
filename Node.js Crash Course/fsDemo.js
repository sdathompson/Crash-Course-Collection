// import fs from 'fs';
import fs from 'fs/promises';

// // readFile() - callback
// // Takes file directory, encoding, and a callback function that runs once the file is read
// fs.readFile('./test.txt', 'utf8', (err, data) => {
//     if (err) throw err;
//     console.log(data);
// });

// // readFileSync() - Synchronous version
// const data = fs.readFileSync('./test.txt', 'utf8');
// console.log(data);

//readFile() = Promise .then() or async-await
fs.readFile('./test.txt','utf8')
.then((data) => console.log(data))
.catch((err) => console.log(err));

//readFile() - async/await - More readable
const readFile = async () => {
    try {
        const data = await fs.readFile('./test.txt', 'utf8');
        console.log(data);
    } catch (error) {
        console.log(error);
    }
};

// writeFile () writes to a file; creates one if it doesn't exist

const writeFile = async () => {
    try {
        let writeFileTest = 'Hello, I am writing to this file';
        await fs.writeFile('./test.txt', writeFileTest);
        console.log('File written to...');
    } catch (error) {
        console.log(error);
    }
};

const appendFile = async () => {
    try {
        // \n is a new line character
        await fs.appendFile('./test.txt', '\n This is appended to the file.-5');
        console.log('File appended to...');
    } catch (error) {
        console.log(error);
    }
};


writeFile();
appendFile();
readFile();