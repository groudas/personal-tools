### Description

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

### Solution
```js
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    const sCopy = [...s]
    for (let i = 0, j = s.length - 1; i < s.length; i++, j--) {
        s[i] = sCopy[j];
    };
    return s
};
```