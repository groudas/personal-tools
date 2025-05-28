### Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

### Solution
```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let cleanS = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    if (cleanS.split('').reverse().join('') == cleanS) {return true}
    return false
};
```