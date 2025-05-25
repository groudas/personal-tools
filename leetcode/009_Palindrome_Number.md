### Description
Given an integer x, return true if x is a palindrome, and false otherwise.

### Solution
```js
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    xString = x.toString();
    if (xString.split("").join() === xString.split("").reverse().join()) {
            return true;
    } else return false;
};
```