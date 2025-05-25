### Description


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Solution
```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {
    for (i = 0; i < nums.length; i++) {
        let subtraction = target - nums[i];
        if (nums.indexOf(subtraction, i + 1) != -1) {
            return [i, nums.indexOf(subtraction, i + 1)];
        }
    }
}
```