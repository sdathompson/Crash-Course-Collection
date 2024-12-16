// More making CLIs (command line interfaces)
console.log(process.argv);

// Run the file in the command line and add flags to the array 
// (i.e. node processDemo.js import pushes import into the array)

console.log(process.argv[3]); //output = 3rd added item to the array

// process.env - system variables
console.log(process.env.LOGNAME);

// pid - the node.js process ID
console.log(process.pid);

//cwd() - the current directory
console.log(process.cwd());

//title
console.log(process.title);

//memory usage
console.log(process.memoryUsage);

// uptime() - uptime of the script execution
console.log(process.uptime());

process.on('exit', (code) => {
    console.log('About to exit with code: ${code}');
});


//exit()
process.exit(0);

console.log('Hello from after exit'); //output = this won't get logged