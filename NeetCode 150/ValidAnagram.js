isAnagram = (s, t) => {
    if (s.length !== t.length) {
        return false;
    }
    const countS = {};
    const countT = {};

    for (let i = 0; i < s.length; i++) {
        //A character is outlined by the key s[i]
        //The value of the key is the number of times the character appears in the string
        countS[s[i]] = (countS[s[i]] || 0) + 1;
        countT[t[i]] = (countT[t[i]] || 0) + 1;
    }
    // Iterate through the hashmaps and make sure the values are the same
    for (let char in countS) {
        if (countS[char] !== countT[char]) {
            return false;
        }
    }
    return true;    
};

console.log(isAnagram("anagram", "nagaram")); 
console.log(isAnagram("rat", "car"));