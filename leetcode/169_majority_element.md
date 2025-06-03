### Description

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### Solution
```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    nums.sort((a, b) => b - a);
    const half = Math.floor(nums.length / 2)
    for (let i = 0; i< nums.length; i++) {
        if (nums[i] === nums[i+half]) {
            return nums[i];
        };
    };
};
```