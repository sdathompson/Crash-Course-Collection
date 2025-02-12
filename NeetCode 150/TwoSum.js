twoSum = (nums, target) => {
    let map = {};
    for (let i = 0; i < nums.length; i++) {
        // Do the two sum in reverse. Difference between target and current number.
        let diff = target - nums[i];
        if (map[diff] !== undefined) {
            return [map[diff], i];
        }
        map[nums[i]] = i;
    }
};

console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]