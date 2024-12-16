import os from 'os';

// userInfo() - information on the current system user
console.log(os.userInfo()); // output = object with the OS system info
// {uid: -1, gid: -1, username: 'sdath', homedir: 'C:\\Users\\sdath', shell: null}

// totalmem() - total memory bank on the device
console.log(os.totalmem()); // output = total memory in bytes
// 16312553472

// freemem() - ram(?)
console.log(os.freemem()); //output = total free memory in bytes

// cpus() - cores for the system
console.log(os.cpus()); //output = object for every core on the system