### Description

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

### Solution
```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    digits[digits.length-1]++;
    for (let i=digits.length-1; i >= 0; i--) {
        if (digits[i] < 10) {
            return digits;
        } else if (!digits[i-1]) {
            digits[i] = 0;
            digits.unshift(1);
            return digits;
        } else {
            digits[i] = 0;
            digits[i-1]++;
        };
    };
};
```