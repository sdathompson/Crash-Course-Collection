import path from 'path';
import url from 'url';

const filePath = './dir1/dir2/test.txt';

// basename()
console.log(path.basename(filePath)); //output = file name in directory 
// "test.txt"

// dirname()
console.log(path.dirname(filePath)); //output = file path 
// "./dir1./dir2"

// extname()
console.log(path.extname(filePath)); //output = extension name 
// ".txt"

// parse()
console.log(path.parse(filePath)); //output = object with all path information
// { root: '', dir: './dir1/dir2', base: 'test.txt', ext: '.txt', name: 'test'};


// To find the file name
const __filename = url.fileURLToPath(import.meta.url); 
const __dirname = path.dirname(__filename);
// console.log(__filename, __dirname);

// join() to pass the parsed directory info as an array (use it to get rid of the /)
// join and construct a path
const filePath2 = path.join(__dirname, 'dir1', 'dir2', 'test.txt');
console.log(filePath2);

// resolve() does a similar thing
const filePath3 = path.resolve(__dirname, 'dir1', 'dir2', 'test.txt');
console.log(filePath3);
