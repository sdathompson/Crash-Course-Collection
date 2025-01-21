hasDuplicate = (nums) => {
    
    const dupeSet = new Set();
    for (const number of nums) {
        if (dupeSet.has(number)) {
            return true;
        }
        dupeSet.add(number);
    }
    return false;
};

console.log(hasDuplicate([1,2,3,4]));
console.log(hasDuplicate([1,2,3,1]));