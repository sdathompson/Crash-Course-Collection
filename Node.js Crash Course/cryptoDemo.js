import crypto from 'crypto';

// createHash() - to hash passwords so you don't directly store passwords in databases
// Initialize the hash
const hash = crypto.createHash('sha256');
// String input of value you want to hash
hash.update('password1234');
// .digest to initialize the hash
console.log(hash.digest('hex'));

//randomBytes() - to generate random cryptographically strong data
crypto.randomBytes(16, (err, buf) => {
    if (err) throw err;
    console.log(buf.toString('hex'));
});