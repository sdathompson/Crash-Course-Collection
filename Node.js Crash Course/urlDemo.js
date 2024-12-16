import url from 'url';

const urlString = "https://www.google.com/search?q=hello+world";

// URL Object
const urlObj = new URL(urlString);
console.log(urlObj); // object containing all the url information


// format () - takes the object and turns it back into a string
console.log(url.format(urlObj)); 

//import.meta.url - file URL - provides the meta data about the current mudle
console.log(import.meta.url);

// fileUrlToPath() - convert the file URL to a regular path
console.log(url.fileURLToPath(import.meta.url));

console.log(urlObj.search);

const params = new URLSearchParams(urlObj.search);
console.log(params.get('q'));
params.append('limit','5');
params.delete('limit');
console.log(params);